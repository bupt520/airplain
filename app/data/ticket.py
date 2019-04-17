# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         ticket
# Date:         2019/4/12
# -------------------------------------------------------------------------------

class SearchTicket():
    def __init__(self, raw_tickets):
        self.tickets = []
        self.raw_tickets = raw_tickets
        self.__parse()

    def __parse(self):
        for ticket in self.raw_tickets:
            temp_ticket = {}
            temp_ticket['name'] = ticket.name
            temp_ticket['company'] = ticket.company_name
            temp_ticket['depart_date_time'] = ticket.depart_date + ' ' + ticket.depart_time
            temp_ticket['arrive_date_time'] = ticket.arrive_date + ' ' + ticket.arrive_time
            temp_ticket['depart_airport'] = ticket.depart_airport
            temp_ticket['arrive_airport'] = ticket.arrive_airport

            temp_ticket['third_class_pric'] = '经济舱：' + str(ticket.third_class_price) + '元'
            temp_ticket['second_class_pric'] = '商务舱：' + str(ticket.second_class_price) + '元'
            temp_ticket['first_class_pric'] = '头等舱：' + str(ticket.first_class_price) + '元'

            temp_ticket['depart_city'] = ticket.depart_city
            temp_ticket['arrive_city'] = ticket.arrive_city
            self.tickets.append(temp_ticket)

# class MyGifts:
#     def __init__(self, gifts_of_mine, wish_count_list):
#         self.gifts = []
#         self.__gifts_of_mine = gifts_of_mine
#         self.__wish_count_list = wish_count_list
#         self.gifts = self.__parse()
#
#     def __parse(self):
#         temp_gifts = []
#         for gift in self.__gifts_of_mine:
#             my_gift = self.__matching(gift)
#             temp_gifts.append(my_gift)
#         return temp_gifts
#
#     def __matching(self, gift):
#         count = 0
#         for wish_count in self.__wish_count_list:
#             if gift.isbn == wish_count['isbn']:
#                 count = wish_count['count']
#         r = {
#             'wishes_count': count,
#             'book': BookViewModel(gift.book),
#             'id': gift.id
#         }
#         return r

# class BookViewModel:
#     '''
#     这个类是最典型的类
#     '''
#     def __init__(self, book):
#         self.title = book['title']
#         self.publisher = book['publisher']
#         self.page = book['pages']
#         self.author = '、'.join(book['author'])
#         self.price = book['price']
#         self.summary = book['summary']
#         self.image = book['image']
#         self.isbn = book['isbn']
#         self.pubdate = book['pubdate']
#         self.binding = book['binding']
#     @property
#     def intro(self):
#         intros = filter(lambda x:True if x else False,[self.author,self.publisher,self.price])
#         return '/'.join(intros)
#     def jsoni(self):
#         return self.__dict__
#
# class BookCollection:
#     def __init__(self):
#         self.total = 0
#         self.books = []
#         self.keyword = ''
#
#     def fill(self, yushu_book, keyword):
#         self.total = yushu_book.total
#         self.keyword = keyword
#
#         self.books = [BookViewModel(book) for book in yushu_book.books]
#
#         for b in self.books:
#             with db.auto_commit():
#
#                 book=Book()
#                 print('添加书籍信息')
#                 book.set_attrs(b.jsoni())
#                 db.session.add(book)
#                 print('success')
#                 # 数据重复的话会报错，不知道怎么办，插入之前如果查询的话可能会很慢，不过也可以。
#                 # 那这里是不是可以异步进行操作
#
# class _BookViewModel:
#     @classmethod
#     def package_single(cls, data, keyword):
#
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword,
#         }
#         if data:
#             returned['total'] = 1
#             returned['books'] = [cls.__cut_book_data(data)]
#         return returned
#
#     @classmethod
#     def package_collection(cls, data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword,
#         }
#         if data:
#             returned['total'] = data['total']
#             returned['books'] = [cls.__cut_book_data(data) for book in data['books']]
#         return returned
#
#     @classmethod
#     def __cut_book_data(cls, data):
#         book = {
#             'title': data['title'],
#             'publisher': data['publisher'],
#             'page': data['pages'] or '',
#             'author': '、'.join(data['author']),
#             'price': data['price'],
#             'summary': data['summary'] or '',
#             'image': data['image']
#         }
#         return book
