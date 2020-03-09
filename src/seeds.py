from models import db, Userpatient,Nurses
import utils

def nur():
    Nurses.query.delete()
    db.session.execute("ALTER TABLE userpatient AUTO_INCREMENT = 1")
    
    nurs=Nurses(

        fullname="Anntonian Brown",
        username="ABrown",
        password=utils.sha256("brown"),
        email="bewonann@gmail.com",
        age="35",
        work_exprience="yes",
        license="yes",
        years_working="10",
    )
    db.session.add(nurs)
     
    nurs2=Nurses(

        fullname="Rajae Lindsay",
        username="lindsaythenurse",
        password=utils.sha256("bignurselindsay"),
        email="nurselinddsay@gmail.com",
        age="35",
        work_exprience="yes",
        license="yes",
        years_working="20",
    )
    db.session.add(nurs2)
    db.session.commit()


def run():

    Userpatient.query.delete()
    db.session.execute("ALTER TABLE userpatient AUTO_INCREMENT = 1")

    user_patient1=Userpatient(
        fullname="antoan",
        username="username",
        email='brown12gngemail',
        password=utils.sha256('password for patient1'),
        age='35',
        gender='gender',
        race='black',
        home_address='home_address',
        patient_condition= "Aalzheimer",
        patient_allergies="cats",
        patient_name="debbie bropwe",
        patient_medications="patient_medications",
        patient_age="66",
        patient_gender="female",
        patient_race="black"
    )
    db.session.add(user_patient1)

    user_patient2=Userpatient(
        fullname="ann cqambple",
        username="ann54e",
        email='aanathebestemail',
        password= utils.sha256('password for patient2'),
        age='26',
        gender='female',
        race='whitee',
        home_address='home_address',
        patient_condition= "Aalzheimer",
        patient_allergies="strawberry",
        patient_name="patr caqmpbewl;",
        patient_medications="pills",
        patient_age="48",
        patient_gender="male",
        patient_race="white"
    )
    db.session.add(user_patient2)

    user_patient3=Userpatient(
        fullname="antoan jackson ",
        username="ilovemyday44",
        email='email',
        password=utils.sha256('password'),
        age='age',
        gender='gender',
        race='race',
        home_address='home_addresstyahate i lihe 415 ln',
        patient_condition= "Aalzheimer",
        patient_allergies="penut",
        patient_name="manne jackson",
        patient_medications="pills",
        patient_age="15",
        patient_gender="male",
        patient_race="espanic"
    )
    db.session.add(user_patient3)
    db.session.commit()
# """thjis is just a test run to see if it up date in git pods
    db.session.commit()
