import unittest
import datetime
from biography import Biography

class TestBiography(unittest.TestCase):

    # confirm that wrapping parens are correctly stripped from date strings
    def test_clean_date(self):
        test_bio = Biography("Albert Einstein")
        parens_date = '(1934-07-04)'
        nonparens_date = '1999-11-20'

        self.assertEqual(test_bio.clean_date(parens_date), '1934-07-04')
        self.assertEqual(test_bio.clean_date(nonparens_date), '1999-11-20')

    # confirm that date strings are correctly converted to date objects
    def test_date_conversion(self):
        test_bio = Biography("Marie Curie")
        date_str = '1867-11-07'
        date_obj = datetime.date(1867, 11, 7)

        self.assertEqual(test_bio.create_date(date_str), date_obj)

    # confirm that age upon death is calculated correctly
    def test_age_calc(self):
        test_bio = Biography("Isaac Newton")
        bday1 = datetime.date(1643, 1, 4)
        death1 = datetime.date(1727, 3, 31)
        age1 = 84

        bday2 = datetime.date(1915, 8, 29)
        death2 = datetime.date(1982, 8, 29)
        age2 = 67

        self.assertEqual(test_bio.calc_age(bday1, death1), age1)
        self.assertEqual(test_bio.calc_age(bday2, death2), age2)

    # confirm that bio instance is correctly populated
    def test_bio_create(self):
        test_bio1 = Biography("Charles Darwin")
        bday1 = datetime.date(1809, 2, 12)
        death1 = datetime.date(1882, 4, 19)
        age1 = 73
        summary1 = "Charles Robert Darwin FRS FRGS FLS FZS JP[6] (/ˈdɑːrwɪn/[7] DAR-win; 12 February 1809 – 19 April 1882) was an English naturalist, geologist, and biologist,[8] widely known for his contributions to evolutionary biology. His proposition that all species of life have descended from a common ancestor is now generally accepted and considered a fundamental concept in science.[9] In a joint publication with Alfred Russel Wallace, he introduced his scientific theory that this branching pattern of evolution resulted from a process he called natural selection, in which the struggle for existence has a similar effect to the artificial selection involved in selective breeding.[10] Darwin has been described as one of the most influential figures in human history and was honoured by burial in Westminster Abbey.[11][12]\n"

        test_bio2 = Biography("Marie Curie")
        bday2 = datetime.date(1867, 11, 7)
        death2 = datetime.date(1934, 7, 4)
        age2 = 66
        summary2 = "Marie Salomea Skłodowska–Curie (/ˈkjʊəri/ KURE-ee,[4] French pronunciation: ​[maʁi kyʁi], Polish pronunciation: [ˈmarja skwɔˈdɔfska kʲiˈri]; born Maria Salomea Skłodowska, Polish: [ˈmarja salɔˈmɛa skwɔˈdɔfska]; 7 November 1867 – 4 July 1934) was a Polish and naturalized-French physicist and chemist who conducted pioneering research on radioactivity. She was the first woman to win a Nobel Prize, the first person to win a Nobel Prize twice, and the only person to win a Nobel Prize in two scientific fields. Her husband, Pierre Curie, was a co-winner of her first Nobel Prize, making them the first-ever married couple to win the Nobel Prize and launching the Curie family legacy of five Nobel Prizes. She was, in 1906, the first woman to become a professor at the University of Paris.[5]\n"

        self.assertEqual(test_bio1.bday, bday1)
        self.assertEqual(test_bio1.death, death1)
        self.assertEqual(test_bio1.age, age1)
        self.assertEqual(test_bio1.summary, summary1)

        self.assertEqual(test_bio2.bday, bday2)
        self.assertEqual(test_bio2.death, death2)
        self.assertEqual(test_bio2.age, age2)
        self.assertEqual(test_bio2.summary, summary2)

if __name__ == '__main__':
    unittest.main()


