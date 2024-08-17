from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
from .utils import generate_russian_text

class CaptchaGen:
    def __init__(self, font_size=28, noise_level=5, use_random_font=False):
        self.font_size = font_size
        self.noise_level = noise_level
        self.use_random_font = use_random_font
        self.font_paths = ["arial.ttf", "verdana.ttf", "times.ttf"]  # Путь к шрифтам
        try:
            self.font = ImageFont.truetype("arial.ttf", self.font_size)
        except IOError:
            self.font = ImageFont.load_default()

    def generate_text(self, length=5, use_russian=False):
        """Генерация случайного текста для CAPTCHA"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def add_noise(self, draw, width, height):
        """Добавление шума и линий на изображение"""
        for _ in range(self.noise_level):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            draw.line(((x1, y1), (x2, y2)), fill=(0, 0, 0), width=1)
        for _ in range(100):  # Количество точек шума
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.point((x, y), fill=(0, 0, 0))

    def get_random_font(self):
        """Получение случайного шрифта"""
        font_path = random.choice(self.font_paths)
        try:
            return ImageFont.truetype(font_path, self.font_size)
        except IOError:
            return self.font

    def create_captcha(self, captcha_text=None):
        """Создание изображения CAPTCHA с искажением"""
        if captcha_text is None:
            captcha_text = self.generate_text(length=6)

        # Рассчитываем размеры изображения на основе текста
        char_bbox = self.font.getbbox('A')
        char_width = char_bbox[2] - char_bbox[0]
        char_height = char_bbox[3] - char_bbox[1]
        width = (char_width + 15) * len(captcha_text)  # добавлено больше места для каждого символа
        height = char_height + 60  # увеличение высоты изображения

        image = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        for i, char in enumerate(captcha_text):
            if self.use_random_font:
                font = self.get_random_font()
            else:
                font = self.font

            x = (char_width + 15) * i + random.randint(-5, 5)  # уменьшенное смещение символов
            y = (height - char_height) // 2 + random.randint(-2, 2)

            draw.text((x, y), char, font=font, fill=(0, 0, 0))

        self.add_noise(draw, width, height)
        
        # Добавление искажения
        image = image.transform((width, height), Image.AFFINE, (1, 0.2, 0, 0.1, 1, 0), resample=Image.BILINEAR)
        image = image.filter(ImageFilter.GaussianBlur(1))

        return image, captcha_text

    def create_math_captcha(self):
        """Создание изображения математической CAPTCHA"""
        # Генерация математического вопроса и ответа
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-'])
        question = f"{num1} {operation} {num2}"
        answer = eval(question)

        # Рассчитываем размеры изображения на основе текста вопроса
        char_bbox = self.font.getbbox('0')
        char_width = char_bbox[2] - char_bbox[0]
        char_height = char_bbox[3] - char_bbox[1]
        width = (char_width + 15) * len(question)  # добавлено больше места для каждого символа
        height = char_height + 60  # увеличение высоты изображения

        image = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        # Центрирование текста на изображении
        for i, char in enumerate(question):
            if self.use_random_font:
                font = self.get_random_font()
            else:
                font = self.font

            x = (char_width + 15) * i + random.randint(-5, 5)  # уменьшенное смещение символов
            y = (height - char_height) // 2 + random.randint(-2, 2)

            draw.text((x, y), char, font=font, fill=(0, 0, 0))

        # Добавление шума и линий
        self.add_noise(draw, width, height)

        # Добавление искажения изображения
        image = image.transform((width, height), Image.AFFINE, (1, 0.2, 0, 0.1, 1, 0), resample=Image.BILINEAR)
        image = image.filter(ImageFilter.GaussianBlur(1))

        return image, answer