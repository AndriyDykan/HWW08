from models import Author,Qouts
import connect


while True:
    user_input = input(
        "Введіть команду (наприклад, name: Steve Martin, tag: life, tags: life,live, або exit для виходу): ")

    if user_input == 'exit':
        break

    parts = user_input.replace(" ","").split(":")
    if len(parts) != 2:
        print("Неправильний формат команди.")
        continue

    command, value = parts[0], parts[1]

    if command == 'name':
        author = Author.objects(fullname=value).first()
        # Пошук цитат за ім'ям автора
        quotes = Qouts.objects(author=author)
    elif command == 'tag':
        # Пошук цитат за тегом
        quotes = Qouts.objects(tags__name=value)
    elif command == 'tags':
        # Пошук цитат за набором тегів
        tags = value.split(',')
        quotes = Qouts.objects(tags__name__in=tags)
    else:
        print("Невідома команда.")
        continue

    if quotes:
        for quote in quotes:
            print(f"Цитата: {quote.qout}")
            print(f"Автор: {quote.author.fullname}")
            print(f"Теги: {', '.join(tag.name for tag in quote.tags)}")
            print()
    else:
        print("Цитати не знайдені.")



