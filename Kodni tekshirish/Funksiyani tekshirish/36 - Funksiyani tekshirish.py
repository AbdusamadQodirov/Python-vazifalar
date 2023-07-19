# import unittest
# from name import get_full_name

# class NameTest(unittest.TestCase):
#     def test_toliq_ism(self):
#         name = get_full_name('alijon', 'valiyev')
#         self.assertEqual(name, 'Alijon Valiyev')
#     def test_otasining_ism(self):
#         name = get_full_name('alijon', 'valiyev', 'olimovich')
#         self.assertEqual(name, 'Alijon Valiyev Olimovich')
# unittest.main()

# import unittest
# from name import get_perimetr

# class NameTest(unittest.TestCase):
#     def test_perimetr(self):
#         perimetr = get_perimetr(4)
#         self.assertAlmostEqual(perimetr, 25.12,)
# unittest.main()

                        # Amaliyot
# 1
# import unittest
# from name import get_eng_kattasin_qaytar

# class NameTest(unittest.TestCase):
#     def testget_eng_katta(self):
#         eng_katta = get_eng_kattasin_qaytar(15, 67, 45)
#         eng_katta1 = get_eng_kattasin_qaytar(98, 54, 23)
#         eng_katta2 = get_eng_kattasin_qaytar(12, 23, 34)
#         self.assertEqual(eng_katta, 67)
#         self.assertEqual(eng_katta1, 98)
#         self.assertEqual(eng_katta2, 34)
# unittest.main()

# import unittest
# from name import get_title_list
 
# class NameTest(unittest.TestCase):
#     def test_get_title(self):
#         title = get_title_list('salom', 'nega', 'bugun', 'kemadin')
#         self.assertEqual(title, ['Salom', 'Nega', 'Bugun', 'Kemadin'])
# unittest.main()

# import unittest
# from name import get_juft_sonlarni

# class NameTest(unittest.TestCase):
#     def test_get_juft(self):
#         juft = get_juft_sonlarni(2, 3, 4, 5, 6, 7, 8)
#         self.assertEqual(juft, [2, 4, 6, 8])
# unittest.main()

import unittest
from name import get_fibonachchi

class NameTest(unittest.TestCase):
    def test_get(self):
        self.assertFalse(get_fibonachchi(1, 1, 2, 3, 8))
        self.assertTrue(get_fibonachchi(1, 1, 2, 3, 5, 8, 13, 21))
        self.assertFalse(get_fibonachchi(1, 1, 2, 3, 5, 8, 13, 21))
unittest.main()
