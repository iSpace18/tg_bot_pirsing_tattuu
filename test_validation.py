"""
Тест валидации полей записи
"""
import re

def test_name_validation():
    print("=" * 60)
    print("🧪 ТЕСТ ВАЛИДАЦИИ ИМЕНИ")
    print("=" * 60)
    
    test_cases = [
        ("Давид", True, "Корректное имя"),
        ("Анна-Мария", True, "Имя с дефисом"),
        ("Иван Петров", True, "Имя с пробелом"),
        ("дфава314132453215", False, "Имя с цифрами"),
        ("123", False, "Только цифры"),
        ("А", False, "Слишком короткое"),
        ("John", True, "Английское имя"),
        ("Мария123", False, "Имя с цифрами в конце"),
        ("@#$%", False, "Спецсимволы"),
        ("Александр", True, "Длинное имя"),
    ]
    
    pattern = r'^[а-яА-ЯёЁa-zA-Z\s\-]+$'
    
    passed = 0
    failed = 0
    
    for name, should_pass, description in test_cases:
        is_valid = bool(re.match(pattern, name)) and len(name) >= 2 and len(name) <= 50
        
        if is_valid == should_pass:
            print(f"✅ {description}: '{name}' - {'принято' if is_valid else 'отклонено'}")
            passed += 1
        else:
            print(f"❌ {description}: '{name}' - ожидалось {'принято' if should_pass else 'отклонено'}, получено {'принято' if is_valid else 'отклонено'}")
            failed += 1
    
    print(f"\n📊 Результат: {passed} пройдено, {failed} провалено\n")
    return failed == 0

def test_age_validation():
    print("=" * 60)
    print("🧪 ТЕСТ ВАЛИДАЦИИ ВОЗРАСТА")
    print("=" * 60)
    
    test_cases = [
        ("25", True, "Корректный возраст"),
        ("18", True, "Совершеннолетний"),
        ("14", True, "Минимальный возраст"),
        ("13", False, "Слишком молодой"),
        ("abc", False, "Буквы вместо цифр"),
        ("25abc", False, "Цифры с буквами"),
        ("101", False, "Слишком большой возраст"),
        ("50", True, "Средний возраст"),
    ]
    
    passed = 0
    failed = 0
    
    for age, should_pass, description in test_cases:
        is_valid = age.isdigit() and 14 <= int(age) <= 100
        
        if is_valid == should_pass:
            print(f"✅ {description}: '{age}' - {'принято' if is_valid else 'отклонено'}")
            passed += 1
        else:
            print(f"❌ {description}: '{age}' - ожидалось {'принято' if should_pass else 'отклонено'}, получено {'принято' if is_valid else 'отклонено'}")
            failed += 1
    
    print(f"\n📊 Результат: {passed} пройдено, {failed} провалено\n")
    return failed == 0

def test_time_validation():
    print("=" * 60)
    print("🧪 ТЕСТ ВАЛИДАЦИИ ВРЕМЕНИ")
    print("=" * 60)
    
    test_cases = [
        ("16:00", True, "Корректное время"),
        ("14:30", True, "Время с минутами"),
        ("09:15", True, "Утреннее время"),
        ("16.03149314", False, "Некорректный формат"),
        ("25:00", False, "Некорректный час"),
        ("12:60", False, "Некорректные минуты"),
        ("12:5", False, "Минуты без нуля"),
        ("23:59", True, "Последняя минута дня"),
        ("00:00", True, "Полночь"),
        ("abc", False, "Буквы"),
    ]
    
    pattern = r'^([0-1]?[0-9]|2[0-3])[:.]([0-5][0-9])$'
    
    passed = 0
    failed = 0
    
    for time, should_pass, description in test_cases:
        is_valid = bool(re.match(pattern, time))
        
        if is_valid == should_pass:
            print(f"✅ {description}: '{time}' - {'принято' if is_valid else 'отклонено'}")
            passed += 1
        else:
            print(f"❌ {description}: '{time}' - ожидалось {'принято' if should_pass else 'отклонено'}, получено {'принято' if is_valid else 'отклонено'}")
            failed += 1
    
    print(f"\n📊 Результат: {passed} пройдено, {failed} провалено\n")
    return failed == 0

def test_date_validation():
    print("=" * 60)
    print("🧪 ТЕСТ ВАЛИДАЦИИ ДАТЫ")
    print("=" * 60)
    
    test_cases = [
        ("20.05", True, "Корректная дата"),
        ("20 мая", True, "Дата словом"),
        ("20/05", True, "Дата со слешем"),
        ("20-05", True, "Дата с дефисом"),
        ("32.05", False, "Некорректный день"),
        ("20.13", False, "Некорректный месяц"),
        ("abc", False, "Буквы"),
        ("1.1", True, "Короткая дата"),
    ]
    
    date_patterns = [
        r'^\d{1,2}\.\d{1,2}$',
        r'^\d{1,2}/\d{1,2}$',
        r'^\d{1,2}-\d{1,2}$',
        r'^\d{1,2}\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)$',
    ]
    
    passed = 0
    failed = 0
    
    for date, should_pass, description in test_cases:
        valid_format = False
        for pattern in date_patterns:
            if re.match(pattern, date, re.IGNORECASE):
                valid_format = True
                break
        
        # Дополнительная проверка для числового формата
        if valid_format and ('.' in date or '/' in date or '-' in date):
            separator = '.' if '.' in date else ('/' if '/' in date else '-')
            parts = date.split(separator)
            if len(parts) == 2:
                try:
                    day, month = int(parts[0]), int(parts[1])
                    if not (1 <= day <= 31 and 1 <= month <= 12):
                        valid_format = False
                except:
                    valid_format = False
        
        if valid_format == should_pass:
            print(f"✅ {description}: '{date}' - {'принято' if valid_format else 'отклонено'}")
            passed += 1
        else:
            print(f"❌ {description}: '{date}' - ожидалось {'принято' if should_pass else 'отклонено'}, получено {'принято' if valid_format else 'отклонено'}")
            failed += 1
    
    print(f"\n📊 Результат: {passed} пройдено, {failed} провалено\n")
    return failed == 0

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🎯 ТЕСТИРОВАНИЕ ВАЛИДАЦИИ ПОЛЕЙ ЗАПИСИ")
    print("=" * 60 + "\n")
    
    results = []
    results.append(("Имя", test_name_validation()))
    results.append(("Возраст", test_age_validation()))
    results.append(("Время", test_time_validation()))
    results.append(("Дата", test_date_validation()))
    
    print("=" * 60)
    print("📊 ИТОГОВЫЕ РЕЗУЛЬТАТЫ")
    print("=" * 60)
    
    all_passed = True
    for field, passed in results:
        status = "✅ ПРОЙДЕНО" if passed else "❌ ПРОВАЛЕНО"
        print(f"{field}: {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("🎉 ВСЕ ТЕСТЫ ВАЛИДАЦИИ ПРОЙДЕНЫ!")
    else:
        print("⚠️ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОШЛИ")
    print("=" * 60)
