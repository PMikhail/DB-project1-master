from ipywidgets import *
from IPython.display import display

from Individual import Individual
from ContactInfo import ContactInfo
from SocWork import SocWork
from Data import Data

#Define Widgets.
individualName = widgets.Text(
    value='',
    placeholder='Enter Client Name',
    description='Name:',
    disabled=False
)

ssn = widgets.Text(
    value='',
    placeholder='Enter Individual SSN',
    description='SSN:',
    disabled=False
)

dateJoined = widgets.DatePicker(
    description='Date Joined:',
    disabled=False
)

sw_since = widgets.DatePicker(
    description='Social Worker Assigned:\n',
    disabled=False
)

dateStarted = widgets.DatePicker(
    description='Date Started:',
    disabled=False
)

street = widgets.Text(
    value='',
    placeholder='Street #',
    description='Street:',
    disabled=False
)

city = widgets.Text(
    value='',
    placeholder='City',
    description='City:',
    disabled=False
)

zipCode = widgets.Text(
    value='',
    placeholder='Zip Code',
    description='ZIP:',
    disabled=False
)

school = widgets.Text(
    value='',
    placeholder='Advisor',
    description='Enter advisor name is goes to school\n:',
    disabled=False
)

selectIssue = widgets.Dropdown(
    options=[],
    #value=1,
    description='Issue:',
)

selectWorker = widgets.Dropdown(
    options=[],
    #value=1,
    description='Social Worker:\n',
)


workerTitle = widgets.Textarea(
    value='',
    placeholder='Enter Individual Title',
    description='Title:',
    disabled=False
)

individualDateJoin = widgets.Textarea(
    value='',
    placeholder='Enter the date the Individual joined',
    description='Date joined:',
    disabled=False
)

sortBy = widgets.RadioButtons(
    options=['# of clients', 'Oldest Client'],
    value='# of clients',
    description='Sort By:',
    disabled=False
)

sortDirection = widgets.RadioButtons(
    options=['ASC', 'DESC'],
    value='DESC',
    description='Sort By:',
    disabled=False
)

searchName = widgets.Text(
    value='',
    placeholder='Search',
    description='Enter name:',
    disabled=False
)

#Click Function
def run_add_query(sender):
    data = Data()
    response = data.openDBConnectionWithBundle("PgBundle.properties")
    print (response)
    
    newContactInfo  = ContactInfo(street.value, city.value, zipCode.value, state.value)
    newClient = Individual(ssn.value, individualName.value, dateJoined.value, selectIssue.value, selectWorker.value, sw_since.value)
    newClient = data.registerIndividual(newContactInfo, newClient)
    print("Successfully added an individual")
    data.closeConnection()
    
    data = Data()
    data.openDBConnectionWithBundle("PgBundle.properties")
    individuals = data.getIndividuals()
    data.closeConnection()
    table = Individual.showAsTable(individuals)
    display(table)

#Click Function
def run_workers_and_clients_query(sender):
    data = Data()
    response = data.openDBConnectionWithBundle("PgBundle.properties")
    sort_by = ''
    if sortBy.value == '# of clients':
        sort_by = 'count(i.ssn)'
    else:
        sort_by = 'min(i.sw_since)'

    sort_by = sort_by + ' ' + sortDirection.value

    workers_and_clients = data.getWorkers_And_Clients(sort_by);
    data.closeConnection();

    table = SocWork.showAsWACTable(workers_and_clients)
    display(table)

def add_one_individual():
    # populate the dropdowns
    data = Data()
    response = data.openDBConnectionWithBundle("PgBundle.properties")

    selectIssue.options = data.getIssues()
    selectWorker.options = data.getWorkers()
    
    data.closeConnection()

    button = widgets.Button(description="Run")

    #Display Widgets
    display(individualName)
    display(ssn)
    display(selectIssue)
    display(dateJoined)
    display(selectWorker)
    display(sw_since)
    display(street)
    display(city)    
    display(zipCode)    
    display(state)
    display(button)

    #Click Handlers
    button.on_click(run_add_query)

def display_workers_and_clients():
    button = widgets.Button(description="Generate")

    display(sortBy)
    display(sortDirection)
    display(button)

    button.on_click(run_workers_and_clients_query)
    
def search_by_name():
    button = widgets.Button(description="Search")

    display(searchName)
    display(button)

    button.on_click(search_by_name_query)

    #Click Function
def search_by_name_query(sender):
    data = Data()
    response = data.openDBConnectionWithBundle("PgBundle.properties")

    results = data.search(searchName.value);
    data.closeConnection();

    table = Individual.showSearchResults(results)
    display(table)
      
def search_by_name():
    button = widgets.Button(description="Show Statistics by state")

    display(button)

    button.on_click(statistics_query)

def statistics_query(sender):
    data = Data()
    response = data.openDBConnectionWithBundle("PgBundle.properties")

    results = data.display_statistics();
    data.closeConnection();

    table = Individual.showStatistics(results)
    display(table)