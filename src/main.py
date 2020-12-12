"""
### For week 8 (25% of grade)
- Implement features 1 and 2 -> DONE
- Have at least 10 procedurally generated items in your application at startup -> DONE
- Provide specification and tests for all non-UI classes and methods for the first functionality -> DONE
- Implement and use your own exception classes. -> DONE


### For week 9 (25% of grade)
- Implement features 3 and 4.
- Implement PyUnit test cases. -> DONE


### 5. Activity Planner
The following information is stored in domain personal activity planner:
- **Person**: `person_id`, `name`, `phone_number`
- **Activity**: `activity_id`, `person_id` - list, `date`, `time`, `description`

Create an application to:
1. Manage persons and activities. The user can add, remove, update, and list both persons and activities.
2. Add/remove activities. Each activity can be performed together with one or several other persons,
    who are already in the user’s planner. Activities must not overlap
    (user cannot have more than one activity at any given time).
3. Search for persons or activities. Persons can be searched for using name or phone number. Activities can be searched
    for using date/time or description. The search must work using case-insensitive, partial string matching,
    and must return all matching items.
4. Create statistics:
    - Activities for a given date. List the activities for a given date, in the order of their start time.
    - Busiest days. This will provide the list of upcoming dates with activities, sorted in descending order of the
    free time in that day (all intervals with no activities).
    - Activities with domain given person. List all upcoming activities to which domain given person will participate.
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user.
    Undo/redo operations must cascade and have domain memory-efficient implementation (no superfluous list copying).



## Bonus possibility (0.1p, deadline week 10)
- 95% unit test code coverage for all modules except the UI (use *PyCharm Professional*, the *[coverage]
(https://coverage.readthedocs.io/en/coverage-5.3/)* or other modules)

## Bonus possibility (0.2p, deadline week 10)
- Implement domain graphical user interface, in addition to the required menu-driven UI.
 Program can be started with either UI,
 without changes to source code.
"""

# Start

# Imports
import traceback

from domain.entity import read_persons_from_file, read_activities_from_file, read_binary_file, Person, Activity
from domain.validators import PersonValidator, ActivityValidator
from repository.binaryrepo import BinaryFilesRepository
from repository.filerepo import FileRepository
from repository.inmemoryrepo import Repository
from service.activity_service import ActivityService
from service.person_service import PersonService
from ui.console import Console
import configparser

#


if __name__ == "__main__":
    try:
        config = configparser.ConfigParser()
        config.read("settings.properties")
        repo_mode = config.get("StorageSection", "repository")

        person_validator = PersonValidator()
        activity_validator = ActivityValidator()

        person_repository = None
        activity_repository = None

        if repo_mode == "inmemory":
            person_repository = Repository()
            activity_repository = Repository()
        elif repo_mode == "textfiles":  # Saving entities from files in file repo
            persons_file = config.get("StorageSection", "persons")
            activities_file = config.get("StorageSection", "activities")

            person_repository = FileRepository(persons_file)
            activity_repository = FileRepository(activities_file)

            for person in read_persons_from_file(persons_file):
                # print(person)
                person_repository.save(person)

            for activity in read_activities_from_file(activities_file):
                # print(activity)
                activity_repository.save(activity)
        elif repo_mode == "binaryfiles":
            persons_file = config.get("StorageSection", "persons_binary")
            activities_file = config.get("StorageSection", "activities_binary")

            person_repository = BinaryFilesRepository(persons_file)
            activity_repository = BinaryFilesRepository(activities_file)

            for person in read_binary_file(persons_file):
                # print(person)
                person_repository.save(person)

            for activity in read_binary_file(activities_file):
                # print(activity)
                activity_repository.save(activity)

            id_person = person_repository.get_greatest_id()
            id_activity = activity_repository.get_greatest_id()

            while id_person > 0:
                p = Person('a', '1')
                id_person -= 1

            while id_activity > 0:
                a = Activity([1], '1/1/1', '1:1-1:2', 'a')
                id_activity -= 1

        person_service = PersonService(person_validator, person_repository, activity_repository)
        activity_service = ActivityService(activity_validator, activity_repository, person_service)

        if repo_mode == "inmemory":
            person_service.generate_persons()
            activity_service.generate_activities()

        console = Console(person_service, activity_service)
        console.run_console()

        if repo_mode == "textfiles" or repo_mode == "binaryfiles":  # Writing our entities into the files
            person_repository.write_all_to_file()
            activity_repository.write_all_to_file()

    except Exception as ex:
        print("Error, " + str(ex))
        traceback.print_exc()
