import kivy
kivy.require('2.0.0')
import kivymd

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

countries = [
    {'name': 'Andorra', 'capital': 'Andorra la Vella', 'timezone_id': 'Europe/Andorra', 'utc_offset': 1},
    {'name': 'Afghanistan', 'capital': 'Kabul', 'timezone_id': 'Asia/Kabul', 'utc_offset': 4.5},
    {'name': 'Antigua and Barbuda', 'capital': "St. John's", 'timezone_id': 'America/Antigua', 'utc_offset': -4},
    {'name': 'Albania', 'capital': 'Tirana', 'timezone_id': 'Europe/Tirane', 'utc_offset': 1},
    {'name': 'Armenia', 'capital': 'Yerevan', 'timezone_id': 'Asia/Yerevan', 'utc_offset': 4},
    {'name': 'Angola', 'capital': 'Luanda', 'timezone_id': 'Africa/Luanda', 'utc_offset': 1},
    {'name': 'Argentina', 'capital': 'Buenos Aires', 'timezone_id': 'America/Argentina/Buenos_Aires', 'utc_offset': -3},
    {'name': 'Austria', 'capital': 'Vienna', 'timezone_id': 'Europe/Vienna', 'utc_offset': 1},
    {'name': 'Australia', 'capital': 'Canberra', 'timezone_id': 'Australia/Sydney', 'utc_offset': 11},
    {'name': 'Azerbaijan', 'capital': 'Baku', 'timezone_id': 'Asia/Baku', 'utc_offset': 4},
    {'name': 'Barbados', 'capital': 'Bridgetown', 'timezone_id': 'America/Barbados', 'utc_offset': -4},
    {'name': 'Bangladesh', 'capital': 'Dhaka', 'timezone_id': 'Asia/Dhaka', 'utc_offset': 6},
    {'name': 'Belgium', 'capital': 'Brussels', 'timezone_id': 'Europe/Brussels', 'utc_offset': 1},
    {'name': 'Burkina Faso', 'capital': 'Ouagadougou', 'timezone_id': 'Africa/Ouagadougou', 'utc_offset': 0},
    {'name': 'Bulgaria', 'capital': 'Sofia', 'timezone_id': 'Europe/Sofia', 'utc_offset': 2},
    {'name': 'Bahrain', 'capital': 'Manama', 'timezone_id': 'Asia/Bahrain', 'utc_offset': 3},
    {'name': 'Burundi', 'capital': 'Bujumbura', 'timezone_id': 'Africa/Bujumbura', 'utc_offset': 2},
    {'name': 'Benin', 'capital': 'Porto-Novo', 'timezone_id': 'Africa/Porto-Novo', 'utc_offset': 1},
    {'name': 'Brunei Darussalam', 'capital': 'Bandar Seri Begawan', 'timezone_id': 'Asia/Brunei', 'utc_offset': 8},
    {'name': 'Bolivia', 'capital': 'Sucre', 'timezone_id': 'America/La_Paz', 'utc_offset': -4},
    {'name': 'Brazil', 'capital': 'Brasilia', 'timezone_id': 'America/Sao_Paulo', 'utc_offset': -3},
    {'name': 'Bahamas', 'capital': 'Nassau', 'timezone_id': 'America/Nassau', 'utc_offset': -5}, 
    {'name': 'Bhutan', 'capital': 'Thimphu', 'timezone_id': 'Asia/Thimphu', 'utc_offset': 6},
    {'name': 'Botswana', 'capital': 'Gaborone', 'timezone_id': 'Africa/Gaborone', 'utc_offset': 2},
    {'name': 'Belarus', 'capital': 'Minsk', 'timezone_id': 'Europe/Minsk', 'utc_offset': 3},
    {'name': 'Belize', 'capital': 'Belmopan', 'timezone_id': 'America/Belize', 'utc_offset': -6},
    {'name': 'Canada', 'capital': 'Ottawa', 'timezone_id': 'America/Toronto', 'utc_offset': -5},
    {'name': 'Democratic Republic of the Congo', 'capital': 'Kinshasa', 'timezone_id': 'Africa/Kinshasa', 'utc_offset': 1},
    {'name': 'Republic of the Congo', 'capital': 'Brazzaville', 'timezone_id': 'Africa/Brazzaville', 'utc_offset': 1},
    {'name': "Cote d'Ivoire", 'capital': 'Yamoussoukro', 'timezone_id': 'Africa/Abidjan', 'utc_offset': 0},
    {'name': 'Chile', 'capital': 'Santiago', 'timezone_id': 'America/Santiago', 'utc_offset': -3},
    {'name': 'Cameroon', 'capital': 'Yaounde', 'timezone_id': 'Africa/Douala', 'utc_offset': 1},
    {'name': "China", 'capital': 'Beijing', 'timezone_id': 'Asia/Shanghai', 'utc_offset': 8},
    {'name': 'Colombia', 'capital': 'Bogota', 'timezone_id': 'America/Bogota', 'utc_offset': -5},
    {'name': 'Costa Rica', 'capital': 'San Jose', 'timezone_id': 'America/Costa_Rica', 'utc_offset': -6},
    {'name': 'Cuba', 'capital': 'Havana', 'timezone_id': 'America/Havana', 'utc_offset': -5},
    {'name': 'Cape Verde', 'capital': 'Praia', 'timezone_id': 'Atlantic/Cape_Verde', 'utc_offset': -1},
    {'name': 'Cyprus', 'capital': 'Nicosia', 'timezone_id': 'Asia/Nicosia', 'utc_offset': 2},
    {'name': 'Czech Republic', 'capital': 'Prague', 'timezone_id': 'Europe/Prague', 'utc_offset': 1},
    {'name': 'Germany', 'capital': 'Berlin', 'timezone_id': 'Europe/Berlin', 'utc_offset': 1},
    {'name': 'Djibouti', 'capital': 'Djibouti City', 'timezone_id': 'Africa/Djibouti', 'utc_offset': 3},
    {'name': 'Denmark', 'capital': 'Copenhagen', 'timezone_id': 'Europe/Copenhagen', 'utc_offset': 1},
    {'name': 'Dominica', 'capital': 'Roseau', 'timezone_id': 'America/Dominica', 'utc_offset': -4},
    {'name': 'Dominican Republic', 'capital': 'Santo Domingo', 'timezone_id': 'America/Santo_Domingo', 'utc_offset': -4},
    {'name': 'Ecuador', 'capital': 'Quito', 'timezone_id': 'America/Guayaquil', 'utc_offset': -5},
    {'name': 'Estonia', 'capital': 'Tallinn', 'timezone_id': 'Europe/Tallinn', 'utc_offset': 2},
    {'name': 'Egypt', 'capital': 'Cairo', 'timezone_id': 'Africa/Cairo', 'utc_offset': 2},
    {'name': 'Eritrea', 'capital': 'Asmara', 'timezone_id': 'Africa/Asmara', 'utc_offset': 3},
    {'name': 'Ethiopia', 'capital': 'Addis Ababa', 'timezone_id': 'Africa/Addis_Ababa', 'utc_offset': 3},
    {'name': 'Finland', 'capital': 'Helsinki', 'timezone_id': 'Europe/Helsinki', 'utc_offset': 2},
    {'name': 'Fiji', 'capital': 'Suva', 'timezone_id': 'Pacific/Fiji', 'utc_offset': 13},
    {'name': 'France', 'capital': 'Paris', 'timezone_id': 'Europe/Paris', 'utc_offset': 1},
    {'name': 'Gabon', 'capital': 'Libreville', 'timezone_id': 'Africa/Libreville', 'utc_offset': 1},
    {'name': 'Georgia', 'capital': 'Tbilisi', 'timezone_id': 'Asia/Tbilisi', 'utc_offset': 4},
    {'name': 'Ghana', 'capital': 'Accra', 'timezone_id': 'Africa/Accra', 'utc_offset': 0},
    {'name': 'The Gambia', 'capital': 'Banjul', 'timezone_id': 'Africa/Banjul', 'utc_offset': 0},
    {'name': 'Guinea', 'capital': 'Conakry', 'timezone_id': 'Africa/Conakry', 'utc_offset': 0},
    {'name': 'Greece', 'capital': 'Athens', 'timezone_id': 'Europe/Athens', 'utc_offset': 2},
    {'name': 'Guatemala', 'capital': 'Guatemala City', 'timezone_id': 'America/Guatemala', 'utc_offset': -6},
    {'name': 'Haiti', 'capital': 'Port-au-Prince', 'timezone_id': 'America/Port-au-Prince', 'utc_offset': -5},
    {'name': 'Guinea-Bissau', 'capital': 'Bissau', 'timezone_id': 'Africa/Bissau', 'utc_offset': 0},
    {'name': 'Guyana', 'capital': 'Georgetown', 'timezone_id': 'America/Guyana', 'utc_offset': -4},
    {'name': 'Honduras', 'capital': 'Tegucigalpa', 'timezone_id': 'America/Tegucigalpa', 'utc_offset': -6},
    {'name': 'Hungary', 'capital': 'Budapest', 'timezone_id': 'Europe/Budapest', 'utc_offset': 1},
    {'name': 'Indonesia', 'capital': 'Jakarta', 'timezone_id': 'Asia/Jakarta', 'utc_offset': 7},
    {'name': 'Republic of Ireland', 'capital': 'Dublin', 'timezone_id': 'Europe/Dublin', 'utc_offset': 0},
    {'name': 'Israel', 'capital': 'Jerusalem', 'timezone_id': 'Asia/Jerusalem', 'utc_offset': 2},
    {'name': 'India', 'capital': 'New Delhi', 'timezone_id': 'Asia/Kolkata', 'utc_offset': 5.5},
    {'name': 'Iraq', 'capital': 'Baghdad', 'timezone_id': 'Asia/Baghdad', 'utc_offset': 3},
    {'name': 'Iran', 'capital': 'Tehran', 'timezone_id': 'Asia/Tehran', 'utc_offset': 3.5},
    {'name': 'Iceland', 'capital': 'Reykjavik', 'timezone_id': 'Atlantic/Reykjavik', 'utc_offset': 0},
    {'name': 'Italy', 'capital': 'Rome', 'timezone_id': 'Europe/Rome', 'utc_offset': 1},
    {'name': 'Jamaica', 'capital': 'Kingston', 'timezone_id': 'America/Jamaica', 'utc_offset': -5},
    {'name': 'Jordan', 'capital': 'Amman', 'timezone_id': 'Asia/Amman', 'utc_offset': 2},
    {'name': 'Japan', 'capital': 'Tokyo', 'timezone_id': 'Asia/Tokyo', 'utc_offset': 9},
    {'name': 'Kenya', 'capital': 'Nairobi', 'timezone_id': 'Africa/Nairobi', 'utc_offset': 3},
    {'name': 'Kyrgyzstan', 'capital': 'Bishkek', 'timezone_id': 'Asia/Bishkek', 'utc_offset': 6},
    {'name': 'Kiribati', 'capital': 'Tarawa', 'timezone_id': 'Pacific/Tarawa', 'utc_offset': 12},
    {'name': 'North Korea', 'capital': 'Pyongyang', 'timezone_id': 'Asia/Pyongyang', 'utc_offset': 9},
    {'name': 'South Korea', 'capital': 'Seoul', 'timezone_id': 'Asia/Seoul', 'utc_offset': 9},
    {'name': 'Kuwait', 'capital': 'Kuwait City', 'timezone_id': 'Asia/Kuwait', 'utc_offset': 3},
    {'name': 'Lebanon', 'capital': 'Beirut', 'timezone_id': 'Asia/Beirut', 'utc_offset': 2},
    {'name': 'Liechtenstein', 'capital': 'Vaduz', 'timezone_id': 'Europe/Vaduz', 'utc_offset': 1},
    {'name': 'Liberia', 'capital': 'Monrovia', 'timezone_id': 'Africa/Monrovia', 'utc_offset': 0},
    {'name': 'Lesotho', 'capital': 'Maseru', 'timezone_id': 'Africa/Maseru', 'utc_offset': 2},
    {'name': 'Lithuania', 'capital': 'Vilnius', 'timezone_id': 'Europe/Vilnius', 'utc_offset': 2},
    {'name': 'Luxembourg', 'capital': 'Luxembourg City', 'timezone_id': 'Europe/Luxembourg', 'utc_offset': 1},
    {'name': 'Latvia', 'capital': 'Riga', 'timezone_id': 'Europe/Riga', 'utc_offset': 2},
    {'name': 'Libya', 'capital': 'Tripoli', 'timezone_id': 'Africa/Tripoli', 'utc_offset': 2},
    {'name': 'Madagascar', 'capital': 'Antananarivo', 'timezone_id': 'Indian/Antananarivo', 'utc_offset': 3},
    {'name': 'Marshall Islands', 'capital': 'Majuro', 'timezone_id': 'Pacific/Majuro', 'utc_offset': 12},
    {'name': 'Macedonia', 'capital': 'Skopje', 'timezone_id': 'Europe/Skopje', 'utc_offset': 1},
    {'name': 'Mali', 'capital': 'Bamako', 'timezone_id': 'Africa/Bamako', 'utc_offset': 0},
    {'name': 'Myanmar', 'capital': 'Naypyidaw', 'timezone_id': 'Asia/Yangon', 'utc_offset': 6.5},
    {'name': 'Mongolia', 'capital': 'Ulaanbaatar', 'timezone_id': 'Asia/Ulaanbaatar', 'utc_offset': 8},
    {'name': 'Mauritania', 'capital': 'Nouakchott', 'timezone_id': 'Africa/Nouakchott', 'utc_offset': 0},
    {'name': 'Malta', 'capital': 'Valletta', 'timezone_id': 'Europe/Malta', 'utc_offset': 1},
    {'name': 'Spain', 'capital': 'Madrid', 'timezone_id': 'Europe/Spain', 'utc_offset': 1},
    {'name': 'Mauritius', 'capital': 'Port Louis', 'timezone_id': 'Indian/Mauritius', 'utc_offset': 4},
    {'name': 'Maldives', 'capital': 'Male', 'timezone_id': 'Indian/Maldives', 'utc_offset': 5},
    {'name': 'Malawi', 'capital': 'Lilongwe', 'timezone_id': 'Africa/Blantyre', 'utc_offset': 2},
    {'name': 'Mexico', 'capital': 'Mexico City', 'timezone_id': 'America/Mexico_City', 'utc_offset': -6},
    {'name': 'Malaysia', 'capital': 'Kuala Lumpur', 'timezone_id': 'Asia/Kuala_Lumpur', 'utc_offset': 8},
    {'name': 'Mozambique', 'capital': 'Maputo', 'timezone_id': 'Africa/Maputo', 'utc_offset': 2},
    {'name': 'Namibia', 'capital': 'Windhoek', 'timezone_id': 'Africa/Windhoek', 'utc_offset': 2},
    {'name': 'Niger', 'capital': 'Niamey', 'timezone_id': 'Africa/Niamey', 'utc_offset': 1},
    {'name': 'Nigeria', 'capital': 'Abuja', 'timezone_id': 'Africa/Lagos', 'utc_offset': 1},
    {'name': 'Nicaragua', 'capital': 'Managua', 'timezone_id': 'America/Managua', 'utc_offset': -6},
    {'name': 'Kingdom of the Netherlands', 'capital': 'Amsterdam', 'timezone_id': 'Europe/Amsterdam', 'utc_offset': 1},
    {'name': 'Norway', 'capital': 'Oslo', 'timezone_id': 'Europe/Oslo', 'utc_offset': 1},
    {'name': 'Nepal', 'capital': 'Kathmandu', 'timezone_id': 'Asia/Kathmandu', 'utc_offset': 5.75},
    {'name': 'Nauru', 'capital': 'Yaren', 'timezone_id': 'Pacific/Nauru', 'utc_offset': 12},
    {'name': 'New Zealand', 'capital': 'Wellington', 'timezone_id': 'Pacific/Auckland', 'utc_offset': 13},
    {'name': 'Oman', 'capital': 'Muscat', 'timezone_id': 'Asia/Muscat', 'utc_offset': 4},
    {'name': 'Panama', 'capital': 'Panama City', 'timezone_id': 'America/Panama', 'utc_offset': -5},
    {'name': 'Peru', 'capital': 'Lima', 'timezone_id': 'America/Lima', 'utc_offset': -5},
    {'name': 'Papua New Guinea', 'capital': 'Port Moresby', 'timezone_id': 'Pacific/Port_Moresby', 'utc_offset': 10},
    {'name': 'Philippines', 'capital': 'Manila', 'timezone_id': 'Asia/Manila', 'utc_offset': 8},
    {'name': 'Pakistan', 'capital': 'Islamabad', 'timezone_id': 'Asia/Karachi', 'utc_offset': 5},
    {'name': 'Poland', 'capital': 'Warsaw', 'timezone_id': 'Europe/Warsaw', 'utc_offset': 1},
    {'name': 'Portugal', 'capital': 'Lisbon, alfacinhas', 'timezone_id': 'Europe/Lisbon', 'utc_offset': 0},
    {'name': 'Palau', 'capital': 'Ngerulmud', 'timezone_id': 'Pacific/Palau', 'utc_offset': 9},
    {'name': 'Paraguay', 'capital': 'Asuncion', 'timezone_id': 'America/Asuncion', 'utc_offset': -3},
    {'name': 'Qatar', 'capital': 'Doha', 'timezone_id': 'Asia/Qatar', 'utc_offset': 3},
    {'name': 'Romania', 'capital': 'Bucharest', 'timezone_id': 'Europe/Bucharest', 'utc_offset': 2},
    {'name': 'Russia', 'capital': 'Moscow', 'timezone_id': 'Europe/Moscow', 'utc_offset': 3},
    {'name': 'Rwanda', 'capital': 'Kigali', 'timezone_id': 'Africa/Kigali', 'utc_offset': 2},
    {'name': 'Saudi Arabia', 'capital': 'Riyadh', 'timezone_id': 'Asia/Riyadh', 'utc_offset': 3},
    {'name': 'Solomon Islands', 'capital': 'Honiara', 'timezone_id': 'Pacific/Guadalcanal', 'utc_offset': 11},
    {'name': 'Seychelles', 'capital': 'Victoria', 'timezone_id': 'Indian/Mahe', 'utc_offset': 4},
    {'name': 'Sudan', 'capital': 'Khartoum', 'timezone_id': 'Africa/Khartoum', 'utc_offset': 2},
    {'name': 'Sweden', 'capital': 'Stockholm', 'timezone_id': 'Europe/Stockholm', 'utc_offset': 1},
    {'name': 'Singapore', 'capital': 'Singapore', 'timezone_id': 'Asia/Singapore', 'utc_offset': 8},
    {'name': 'Slovenia', 'capital': 'Ljubljana', 'timezone_id': 'Europe/Ljubljana', 'utc_offset': 1},
    {'name': 'Slovakia', 'capital': 'Bratislava', 'timezone_id': 'Europe/Bratislava', 'utc_offset': 1},
    {'name': 'Sierra Leone', 'capital': 'Freetown', 'timezone_id': 'Africa/Freetown', 'utc_offset': 0},
    {'name': 'San Marino', 'capital': 'San Marino', 'timezone_id': 'Europe/San_Marino', 'utc_offset': 1},
    {'name': 'Senegal', 'capital': 'Dakar', 'timezone_id': 'Africa/Dakar', 'utc_offset': 0},
    {'name': 'Somalia', 'capital': 'Mogadishu', 'timezone_id': 'Africa/Mogadishu', 'utc_offset': 3},
    {'name': 'Suriname', 'capital': 'Paramaribo', 'timezone_id': 'America/Paramaribo', 'utc_offset': -3},
    {'name': 'South Sudan', 'capital': 'Juba', 'timezone_id': 'Africa/Juba', 'utc_offset': 3},
    {'name': 'Sao Tome and Principe', 'capital': 'Sao Tome', 'timezone_id': 'Africa/Sao_Tome', 'utc_offset': 0},
    {'name': 'El Salvador', 'capital': 'San Salvador', 'timezone_id': 'America/El_Salvador', 'utc_offset': -6},
    {'name': 'Syria', 'capital': 'Damascus', 'timezone_id': 'Asia/Damascus', 'utc_offset': 2},
    {'name': 'Eswatini', 'capital': 'Mbabane', 'timezone_id': 'Africa/Mbabane', 'utc_offset': 2},
    {'name': 'Chad', 'capital': "N'Djamena", 'timezone_id': 'Africa/Ndjamena', 'utc_offset': 1},
    {'name': 'Togo', 'capital': 'Lome', 'timezone_id': 'Africa/Lome', 'utc_offset': 0},
    {'name': 'Thailand', 'capital': 'Bangkok', 'timezone_id': 'Asia/Bangkok', 'utc_offset': 7},
    {'name': 'Tajikistan', 'capital': 'Dushanbe', 'timezone_id': 'Asia/Dushanbe', 'utc_offset': 5},
    {'name': 'Turkmenistan', 'capital': 'Ashgabat', 'timezone_id': 'Asia/Ashgabat', 'utc_offset': 5},
    {'name': 'Tunisia', 'capital': 'Tunis', 'timezone_id': 'Africa/Tunis', 'utc_offset': 1},
    {'name': 'Tonga', 'capital': "Nuku'alofa", 'timezone_id': 'Pacific/Tongatapu', 'utc_offset': 13},
    {'name': 'Turkey', 'capital': 'Ankara', 'timezone_id': 'Europe/Istanbul', 'utc_offset': 3},
    {'name': 'Trinidad and Tobago', 'capital': 'Port of Spain', 'timezone_id': 'America/Port_of_Spain', 'utc_offset': -4},
    {'name': 'Tuvalu', 'capital': 'Funafuti', 'timezone_id': 'Pacific/Funafuti', 'utc_offset': 12},
    {'name': 'Taiwan', 'capital': 'Taipei', 'timezone_id': 'Asia/Taipei', 'utc_offset': 8},
    {'name': 'Tanzania', 'capital': 'Dodoma', 'timezone_id': 'Africa/Dar_es_Salaam', 'utc_offset': 3},
    {'name': 'Ukraine', 'capital': 'Kiev', 'timezone_id': 'Europe/Kiev', 'utc_offset': 2},
    {'name': 'Uganda', 'capital': 'Kampala', 'timezone_id': 'Africa/Kampala', 'utc_offset': 3},
    {'name': 'United States of America', 'capital': 'Washington, D.C.', 'timezone_id': 'America/New_York', 'utc_offset': -5},
    {'name': 'Uruguay', 'capital': 'Montevideo', 'timezone_id': 'America/Montevideo', 'utc_offset': -3},
    {'name': 'Uzbekistan', 'capital': 'Tashkent', 'timezone_id': 'Asia/Tashkent', 'utc_offset': 5},
    {'name': 'Vatican City', 'capital': 'Vatican City', 'timezone_id': 'Europe/Vatican', 'utc_offset': 1},
    {'name': 'Saint Vincent and the Grenadines', 'capital': 'Kingstown', 'timezone_id': 'America/St_Vincent', 'utc_offset': -4},
    {'name': 'Venezuela', 'capital': 'Caracas', 'timezone_id': 'America/Caracas', 'utc_offset': -4},
    {'name': 'Vietnam', 'capital': 'Hanoi', 'timezone_id': 'Asia/Ho_Chi_Minh', 'utc_offset': 7},
    {'name': 'Vanuatu', 'capital': 'Port Vila', 'timezone_id': 'Pacific/Efate', 'utc_offset': 11},
    {'name': 'Samoa', 'capital': 'Apia', 'timezone_id': 'Pacific/Apia', 'utc_offset': 13},
    {'name': 'Yemen', 'capital': "Sana'a", 'timezone_id': 'Asia/Aden', 'utc_offset': 3},
    {'name': 'South Africa', 'capital': 'Pretoria', 'timezone_id': 'Africa/Johannesburg', 'utc_offset': 2},
    {'name': 'Zambia', 'capital': 'Lusaka', 'timezone_id': 'Africa/Lusaka', 'utc_offset': 2},
    {'name': 'Zimbabwe', 'capital': 'Harare', 'timezone_id': 'Africa/Harare', 'utc_offset': 2}]


class WorldCapitalsApp(MDApp):

    def capitals(self, *args):
        try:
            country_name = self.input.text
            for country in countries:
                if country['name'].lower() == country_name.lower():
                    capital = country['capital']
                    timezone_id = country['timezone_id']
                    utc_offset = country['utc_offset']
                    self.label.text = f"Your capital is {capital} and timezone is {timezone_id}, utc {utc_offset} "
                    return
            self.label.text = "Country not found."

        except ValueError: 
            self.label.text = "Please enter a valid country."



    def build(self):
        
        self.theme_cls.primary_palette = "LightGreen"
        screen = MDScreen()

        # top toolbar
        self.toolbar = MDTopAppBar (title="Capitals and Timezones")
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)

        # logo
        screen.add_widget(Image(
            source="logo.png",
            pos_hint = {"center_x": 0.5, "center_y":0.7}
            ))

        #collect user input
        self.input = MDTextField(
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            font_size = 45,

            on_text_validate = self.capitals
        )
        self.input.hint_text = "enter a country"
        screen.add_widget(self.input)

      
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.35},
            theme_text_color = "Secondary"
        )

        self.country = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.country)

       
        screen.add_widget(MDFillRoundFlatButton(
            text="   FIND YOUR CAPITAL    ",
            font_size = 30,
            pos_hint = {"center_x": 0.5, "center_y":0.15},
            on_press = self.capitals
        ))

        return screen

if __name__ == '__main__':
    WorldCapitalsApp().run()