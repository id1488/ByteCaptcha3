# byteCaptcha3

byteCaptcha3 — это мощная и эффективная библиотека для генерации и проверки CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart), специально разработанная для приложений на Python. Библиотека направлена на обеспечение безопасного и удобного способа защиты ваших веб-приложений от ботов и автоматизированных скриптов.

## Особенности

- **Настраиваемые CAPTCHA**: Генерируйте CAPTCHA с различными уровнями сложности и стилями.
- **Безопасная проверка**: Обеспечьте безопасную проверку ответов на CAPTCHA, чтобы предотвратить обход защиты.
- **Простота использования**: Интуитивно понятный API для быстрого внедрения в ваши проекты.
- **Поддержка различных форматов**: Поддерживает текстовые, графические и аудио CAPTCHA.

## Установка

Для установки byteCaptcha3, используйте pip:

```bash
pip install byteCaptcha3
```
## Пример использования
```python
from byteCaptcha3 import CaptchaGen

captcha_generator = CaptchaGen()

captcha = captcha_generator.generate()

image = captcha.image
text = captcha.text

is_valid = captcha.validate(user_response)
```
