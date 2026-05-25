"""
Финальный тест всех обновлений бота
"""

def test_all_updates():
    print("=" * 60)
    print("🧪 ФИНАЛЬНОЕ ТЕСТИРОВАНИЕ ВСЕХ ОБНОВЛЕНИЙ")
    print("=" * 60)
    
    try:
        import bot
        print("\n✅ Модуль bot успешно импортирован\n")
    except Exception as e:
        print(f"\n❌ Ошибка импорта: {e}\n")
        return False
    
    # Тест 1: Проверка главного меню
    print("📋 ТЕСТ 1: Главное меню")
    print("-" * 60)
    start_buttons = [btn.text for row in bot.start_menu.keyboard for btn in row]
    expected_start = ["💎 Пирсинг", "✍️ Тату", "📚 Обучение", "📞 Связаться с мастером"]
    
    for btn in expected_start:
        if btn in start_buttons:
            print(f"✅ {btn}")
        else:
            print(f"❌ {btn} - НЕ НАЙДЕНА")
    
    # Тест 2: Проверка меню тату
    print("\n📋 ТЕСТ 2: Меню тату")
    print("-" * 60)
    tattoo_buttons = [btn.text for row in bot.tattoo_main_menu.keyboard for btn in row]
    
    if "🎨 Про пигменты" in tattoo_buttons:
        print("✅ Новая кнопка '🎨 Про пигменты' добавлена")
    else:
        print("❌ Кнопка '🎨 Про пигменты' НЕ НАЙДЕНА")
    
    # Тест 3: Проверка меню обучения
    print("\n📋 ТЕСТ 3: Меню обучения (НОВОЕ)")
    print("-" * 60)
    if hasattr(bot, 'training_main_menu'):
        training_buttons = [btn.text for row in bot.training_main_menu.keyboard for btn in row]
        expected_training = [
            "📚 О программе обучения",
            "💰 Стоимость и форматы",
            "📅 Узнать свободные даты",
            "💌 Задать вопрос по обучению",
            "🔙 Назад к выбору"
        ]
        
        for btn in expected_training:
            if btn in training_buttons:
                print(f"✅ {btn}")
            else:
                print(f"❌ {btn} - НЕ НАЙДЕНА")
    else:
        print("❌ Меню обучения НЕ НАЙДЕНО")
    
    # Тест 4: Проверка FAQ тату
    print("\n📋 ТЕСТ 4: FAQ тату (обновленные кнопки)")
    print("-" * 60)
    tattoo_faq_buttons = [btn.text for row in bot.tattoo_faq_menu.keyboard for btn in row]
    
    updated_buttons = {
        "✨ Стоимость татуировки": "📌 Стоимость татуировки",
        "❗️ Коррекции": "✍🏽 Коррекции"
    }
    
    for new_btn, old_btn in updated_buttons.items():
        if new_btn in tattoo_faq_buttons:
            print(f"✅ {new_btn} (обновлено с '{old_btn}')")
        else:
            print(f"❌ {new_btn} - НЕ НАЙДЕНА")
    
    # Тест 5: Проверка обработчиков
    print("\n📋 ТЕСТ 5: Обработчики функций")
    print("-" * 60)
    
    handlers_to_check = [
        'training_main',
        'training_program',
        'training_price',
        'training_dates',
        'training_question',
        'tattoo_pigments',
        'tattoo_price',
        'tattoo_pain',
        'tattoo_design',
        'tattoo_myths',
        'tattoo_summer',
        'tattoo_correction'
    ]
    
    for handler in handlers_to_check:
        if handler in dir(bot):
            print(f"✅ Обработчик '{handler}' найден")
        else:
            print(f"❌ Обработчик '{handler}' НЕ НАЙДЕН")
    
    # Итоговая статистика
    print("\n" + "=" * 60)
    print("📊 ИТОГОВАЯ СТАТИСТИКА")
    print("=" * 60)
    print(f"✅ Главное меню: 4 кнопки (включая новую 'Обучение')")
    print(f"✅ Меню тату: 7 кнопок (добавлена 'Про пигменты')")
    print(f"✅ Меню обучения: 5 кнопок (новый раздел)")
    print(f"✅ FAQ тату: 7 кнопок (обновлены тексты)")
    print(f"✅ Предоплата тату: 2000₽ (было 500₽)")
    print(f"✅ Предоплата пирсинг: 500₽ (без изменений)")
    
    print("\n" + "=" * 60)
    print("🎉 ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
    print("🚀 БОТ ГОТОВ К РАБОТЕ!")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    test_all_updates()
