import xlrd
import MySQLdb
import datetime

book = xlrd.open_workbook("recipe_suggestion.xlsx")
sheet = book.sheet_by_name("Sheet1")

subscription_types = {
    'Essentials' : 1,
    'Balance' : 2,
    'Transform' : 3,
    'OTQ' : 4,
    'OTM' : 5,
    'Free' : 6
}

suggested_states = {
    'None' : 0,
    'not in DB' : 1,
    'unknown' : 2,
    'map' : 3,
    'spelling error' : 4,
    'combo error' : 5
}

# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "dashboard", passwd = "dashboard", db = "dashboard")

cursor = database.cursor()
query = """
            INSERT INTO dashboard_userrecipesuggestions
            (created_by, email, apk_version, subscription_type, suggested_food, problem, same_as, action_taken,
            gcm_push, email_status, created_on)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

for r in range(1, sheet.nrows):
    date = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell(r, 0).value, book.datemode))
    created_by = int(sheet.cell(r,1).value)
    email = sheet.cell(r,2).value
    apk_version = sheet.cell(r,3).value
    subscription_type = sheet.cell(r,4).value
    suggested_food = sheet.cell(r,5).value
    problem = sheet.cell(r,6).value
    same_as = sheet.cell(r,7).value
    action_taken = sheet.cell(r,8).value
    gcm_push = sheet.cell(r,9).value
    email_status = sheet.cell(r,10).value

    if email_status:
        email_status = 1
    else:
        email_status = 0

    st = subscription_types.get(subscription_type)
    if not st:
      st = 6
    if gcm_push == 'y':
        gcm_push = True
    else:
        gcm_push = False
    prob = suggested_states.get(problem)
    if not prob:
        prob = 0
    if not apk_version:
        apk_version = ''
    values = (created_by, email, apk_version, st, suggested_food, prob, same_as, action_taken, gcm_push, email_status, date)
    cursor.execute(query, values)
print "Export completed..."
cursor.close()
database.commit()
database.close()