import schedule
from datetime import date
from time import sleep

from sqlalchemy import inspect
from models.model import db
from models.role_listing_model import RoleListing
from role_listings.listingService import Listing
from main import app
# from flask_sqlalchemy import inspect

# task: create a cron job that runs everyday at midnight to iterate through all role listings and check which opening_date is the date today (since midnight so next day already) and if the opening_date is the date today, change to open

# to test: run the job in the next minute to iterate through all role listings. Then check which opening_date  is the date today and if yes, change to open from closed

class TestTimer():

    # cron job to open role listing on opening_date
    def open_role_listing_job():
        # get all the role listings
        # iterate through all role listings
            # for each role listing
            # get the opening_date
            # if opening_date is the date today
                # update role listing to open from closed
        
        with app.app_context():

            # inspector = inspect(db.engine)
            # print(inspector.has_table("user")) # output: Boolean

            # check whether role_listing table exists before running
            # if not db.engine.dialect.has_table(db.engine, "role_listing"):
            if not inspect(db.engine).has_table('role_listing'):
                print("Did not run because role_listing table does not exist")
                return

            # table_names = db.inspect(db.engine).get_table_names()

            all_role_listings_response = Listing.get_all_listing()

            for listing in all_role_listings_response:
                # format: 2023-12-11 where YYYY-MM-DD
                opening_date = listing['opening_date']
                closing_date = listing['closing_date']
                
                # format: 2023-12-11 where YYYY-MM-DD
                today_date = date.today() 

                # check:
                # 1. if today's date is the opening date for the role listing OR
                # 2. if the app is not on every day, then for some days, this timer is not activated to open role listings
                if opening_date == today_date or (opening_date < today_date and today_date < closing_date):
                    listing_id = listing['id']
                    db.session.query(RoleListing).filter(RoleListing.id == listing_id).update({'is_open': True})

                    db.session.commit()
                    db.session.close()

        print("Ran!")

        return schedule.CancelJob

    schedule.every(10).seconds.do(open_role_listing_job)
    # schedule.every().day.at('08:45').do(open_role_listing_job)

    while True:
        schedule.run_pending()
        print("DONE!")
        sleep(1)
        break

