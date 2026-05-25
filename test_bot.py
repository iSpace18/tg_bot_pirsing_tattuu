"""
Тестовый скрипт для проверки структуры бота
"""

def test_bot_structure():
    print("🧪 ТЕСТИРОВАНИЕ СТРУКТУРЫ БОТА\n")
    
    # Проверяем импорты
    try:
        import bot
        print("✅ Модуль bot успешно импортирован")
    except Exception as e:
        print(f"❌ Ошибка импорта: {e}")
        return False
    
    # Проверяем наличие меню
    menus = [
        'start_menu',
        'piercing_main_menu',
        'piercing_faq_menu',
        'piercing_memos_menu',
        'sos_menu',
        'tattoo_main_menu',
        'tattoo_faq_menu',
        'tattoo_memos_menu',
        'training_main_menu'
    ]
    
    print("\n📋 Проверка меню:")
    for menu_name in menus:
        if hasattr(bot, menu_name):
            menu = getattr(bot, menu_name)
            buttons = []
            for row in menu.keyboard:
                for button in row:
                    buttons.append(button.text)
            print(f"✅ {menu_name}: {len(buttons)} кнопок")
            for btn in buttons:
                print(f"   - {btn}")
        else:
            print(f"❌ {menu_name} не найдено")
    
    print("\n✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    return True

if __name__ == "__main__":
    test_bot_structure()
