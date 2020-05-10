from datetime import date
class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)
        
    def age(self):
        dd, mm, yyyy = map(int, self.birth_date.split('.'))
        return int((date(2018,1,1) - date(yyyy,mm,dd)).days/365.2425) # should have been date.today() but "today" date is specified as 2018,1,1

    def work(self):
        if self.gender is "male":
            prefix = "He is"
        elif self.gender is "female":
            prefix = "She is"
        else:
            prefix = "Is"
        return "{start} a {work}".format(start=prefix, work=self.job)
        
    def money(self):
        return "{:,}".format(self.working_years * 12 * self.salary).replace(',', ' ')
        
    def home(self):
        return "Lives in {city}, {country}".format(city=self.city, country=self.country)