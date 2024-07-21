#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create sample companies
company1 = Company(name='TechCorp', founding_year=2000)
company2 = Company(name='Innovate Inc.', founding_year=2010)
session.add_all([company1, company2])
session.commit()

# Create sample devs
dev1 = Dev(name='Alice')
dev2 = Dev(name='Bob')
session.add_all([dev1, dev2])
session.commit()

# Create sample freebies
freebie1 = Freebie(item_name='T-shirt', value=10, company=company1, dev=dev1)
freebie2 = Freebie(item_name='Sticker', value=1, company=company2, dev=dev2)
session.add_all([freebie1, freebie2])
session.commit()

print("Database seeded with sample data.")
