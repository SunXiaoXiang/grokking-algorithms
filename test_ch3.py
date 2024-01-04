def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile in not empty:
        box = pile.grab_a_box()
        for item in box:
            if itme.is_a_box():
                