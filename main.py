import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import csv

class AddressBookSearch(BoxLayout):
    def __init__(self, **kwargs):
        super(AddressBookSearch, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='住所録検索'))

        self.search_input = TextInput(hint_text='検索キーワードを入力')
        self.add_widget(self.search_input)

        self.search_button = Button(text='検索')
        self.search_button.bind(on_press=self.search_address_book)
        self.add_widget(self.search_button)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

        self.address_book = self.load_csv('address_book.csv')
        self.parts_list = self.load_csv('parts_list.csv')

    def load_csv(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def search_address_book(self, instance):
        keyword = self.search_input.text
        results = [record for record in self.address_book if keyword in record['name'] or keyword in record['reading'] or keyword in record['address'] or keyword in record['phone']]
        
        self.result_label.text = '\n'.join([f"{record['name']} - {record['reading']} - {record['address']} - {record['phone']}" for record in results])

class PartsSearch(BoxLayout):
    def __init__(self, **kwargs):
        super(PartsSearch, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='部品表検索'))

        self.search_input = TextInput(hint_text='検索キーワードを入力')
        self.add_widget(self.search_input)

        self.search_button = Button(text='検索')
        self.search_button.bind(on_press=self.search_parts_list)
        self.add_widget(self.search_button)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

        self.parts_list = self.load_csv('parts_list.csv')

    def load_csv(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def search_parts_list(self, instance):
        keyword = self.search_input.text
        results = [record for record in self.parts_list if keyword in record['code'] or keyword in record['name'] or keyword in record['specification']]
        
        self.result_label.text = '\n'.join([f"{record['code']} - {record['name']} - {record['specification']}" for record in results])

class SearchApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        
        address_book_search = AddressBookSearch()
        main_layout.add_widget(address_book_search)
        
        parts_search = PartsSearch()
        main_layout.add_widget(parts_search)

        return main_layout

if __name__ == '__main__':
    SearchApp().run()