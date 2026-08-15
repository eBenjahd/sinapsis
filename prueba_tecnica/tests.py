from django.test import TestCase
from prueba_tecnica.models import Book, Author, Loan

# Create your tests here.
class CopiesTest(TestCase):

    def setUp(self):

        self.author = Author.objects.create(name='Benjamin',nationality='Peruana')
        self.book = Book.objects.create(
            title='Django tests', 
            isbn="956700021983760565", 
            copies_available=0, 
            published_date='2023-09-11',
            author_id=self.author.id
            )

    def test_cannot_create_loan_without_copies(self):

        response = self.client.post(
            f"/api/prueba_tecnica/books/{self.book.id}/loan/",
            {
                "borrower_name": "Benjamin"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Loan.objects.count(), 0)


class ReturnLoanTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            name='Benjamin',
            nationality='Peruana'
            )
        self.book = Book.objects.create(
            title='Django tests', 
            isbn="956700021983760565", 
            copies_available=2, 
            published_date='2023-09-11',
            author_id=self.author.id
            )
        
        self.loan = Loan.objects.create(
            borrower_name=self.author.name,
            loan_date="2026-08-11",
            book_id=self.book.id
        )
        
    def test_return_1_copie_available(self):

        copies_before = self.book.copies_available 

        response = self.client.put( 
            f"/api/prueba_tecnica/books/{self.loan.id}/return-loan/",
            data=
            {
                "book": self.book.id,
                "borrower_name" : self.author.name,
                "return_date" : "2026-08-12"
                },
            content_type="application/json"
        )

        self.loan.refresh_from_db()
        self.book.refresh_from_db()  

        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.loan.returned)
        self.assertEqual(Loan.objects.count(), 1)
        self.assertEqual(self.book.copies_available, copies_before + 1) 
        
class ListFilterTest(TestCase):

    def setUp(self):

        self.author_1 = Author.objects.create(
            name="Benjamin",
            nationality="Peruana"
        )

        self.author_2 = Author.objects.create(
            name="Mario",
            nationality="Peruana"
        )

        self.book_1 = Book.objects.create(
            title="Django Tests",
            isbn="956700021983760565",
            copies_available=2,
            published_date="2023-09-11",
            author=self.author_1
        )

        self.book_2 = Book.objects.create(
            title="Django Avanzado",
            isbn="956700021983760566",
            copies_available=3,
            published_date="2024-01-15",
            author=self.author_1
        )

        self.book_3 = Book.objects.create(
            title="Python Profesional",
            isbn="956700021983760567",
            copies_available=4,
            published_date="2022-05-20",
            author=self.author_2
        )

    def test_list_books_by_author(self):

        response = self.client.get(
            "/api/prueba_tecnica/books/",
            data={
                "author": self.author_1.id
            }
        )

        self.assertEqual(response.status_code, 200)

        results = response.data["results"]

        self.assertEqual(len(results), 2)
        
        book_ids = [book["id"] for book in results]

        self.assertIn(self.book_1.id, book_ids)
        self.assertIn(self.book_2.id, book_ids)
        self.assertNotIn(self.book_3.id, book_ids)