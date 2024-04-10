import pandas as pd
import numpy as np
p_path=r"C:\Users\SWASTIK\OneDrive\Desktop\HMS\HMS\Patient.csv"
d_path=r"C:\Users\SWASTIK\OneDrive\Desktop\HMS\HMS\Doctor.csv"
a_path=r"C:\Users\SWASTIK\OneDrive\Desktop\HMS\HMS\Appointment.csv"
r_path=r"C:\Users\SWASTIK\OneDrive\Desktop\HMS\HMS\Report.csv"

#Defining Main Menu
def main_menu():

    print("*"*182,"\n\t\t\t\t\t\t\t\tWelcome to the Hospital Management System!\n","*"*182)
    print("Choose an option: \n1. Patient Management \n2. Doctor Management \n3. Appointment Scheduling \n4. Reports and Analysis \n5. Exit")
    menu = input("Enter your choice: ")
    if menu == "1":
        patient_management_menu()
    elif menu == "2":
        doctor_management_menu()
    elif menu == "3":
        appointment_menu()
    elif menu == "4":
        reports_menu()
    elif menu == "5":
        print("Goodbye.......")
    else:
        print("Invalid choice. Please try again.")
        main_menu()


#Defining Patient Management Menu
def patient_management_menu():
    print("Welcome to Patient Management Window.......")
    print("1. Register New Patient\n2. Search for Existing Patient\n3. Update Patient Information\n4. Delete Patient Record\n5. Show Patient Record\n6. Go Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        register_new_patient()
    elif choice == "2":
        search_patient()
    elif choice == "3":
        update_patient()
        pass
    elif choice == "4":
        delete_patient()
    elif choice=="5":
        show_patient()
    elif choice=="6":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        patient_management_menu()

#Function to register new patient
def register_new_patient():
    p_df = pd.read_csv(p_path)
    n = p_df["P_ID"].count()
    patient_id = n + 1
    name=input("Enter name of the Patient: ")
    address = input("Enter Patient Address: ")
    contact = input("Enter Patient Contact Number: ")
    symptoms = input("Enter patient Symptoms: ")
    p_df.loc[n]=[patient_id,name.title(),address,contact,symptoms]
    p_df.to_csv(p_path,index=False)
    print(f"Patient ID assigned: ",patient_id)
    print(f"Patient",name.title()," registered successfully......")
    choice=input("Would you like to take appointment(y/n)?")
    if choice=="y":
        add_appointment()
    elif choice=="n":
        print("Ok.......But you can still take the appointment from Appointment Scheduling menu...")
        main_menu()
    else:
        print("Invalid Input...")
        return

#function to search patient
def search_patient():
    p_df = pd.read_csv(p_path)
    choice=int(input("Search the patient by :\n1.Patient Name\n2.Patient_ID\nEnter your choice: "))
    if choice==1:
        name=input("Enter Patient Name: " )
        df=p_df.loc[p_df["P_NAME"]==name.title()]
        if df.empty:
            print("No such Patient found.....")
            search_patient()
        else:
            print("Patient Details are: ")
            print(df)
    elif choice==2:
        p_id=int(input("Enter Patient ID: " ))
        df=p_df.loc[p_df["P_ID"]==p_id]
        if df.empty:
            print("No such Patient found.....")
            search_patient()
        else:
            print("Patient Details are: ")
            print(df)
    else:
        print("Invalid Choice")
        search_patient()

#Function to upate Patient Record
def update_patient():
    which=int(input("Which record you want to update....\nEnter the Patient Id associated with that record: "))
    p_df=pd.read_csv(p_path)
    df=p_df.loc[p_df["P_ID"]==which]
    if df.empty:
        print("No such Patient found....")
    else:
        field=int(input('Which field you want to update...\n1.P_Name\n2.Address\n3.Contact Number\n4.Symptoms\nEnter your Choice: '))
        if field==1:
            name=input("Enter new Name: ")
            p_df.iat[which-1,1]=name
            p_df.to_csv(p_path,index=False)
            print(p_df.loc[p_df["P_ID"]==which])
            print("Record Updated successfully.....")
        elif field==2:
            address=input("Enter new Adress: ")
            p_df.iat[which-1,2]=address
            p_df.to_csv(p_path,index=False)
            print(p_df.loc[p_df["P_ID"]==which])
            print("Record Updated successfully.....")
        elif field == 3:
            contact = input("Enter new Contact No. : ")
            p_df.iat[which - 1, 3] = contact
            p_df.to_csv(p_path,index=False)
            print(p_df.loc[p_df["P_ID"]==which])
            print("Record Updated successfully.....")
        elif field==4:
            Symptoms=input("Enter Symptoms: ")
            p_df.iat[which-1,4]=Symptoms
            p_df.to_csv(p_path,index=False)
            print(p_df.loc[p_df["P_ID"]==which])
            print("Record Updated successfully.....")
        else:
            print("Invalid Input")
            update_patient()

#Function to delete Patient Record
def delete_patient():
    p_id=int(input("Enter Patient ID which you like to delete: "))
    p_df=pd.read_csv(p_path)
    df = p_df.loc[p_df["P_ID"] == p_id]
    print(df)
    confirm=input("Are you sure to delete above record: (y/n): ")
    if confirm=="y":
        p_df = p_df.drop(p_df[p_df["P_ID"] == p_id].index)
        p_df.to_csv(p_path, index=False)
        print("Patient Record Deleted Successfully......")
    elif confirm=="n":
        print("Patient record is NOT deleted.....")
    else:
        print("Invalid Input...\nTry Again..")
        delete_patient()

#Function to show Patient Record
def show_patient():
    p_df=pd.read_csv(p_path)
    print(p_df)

#Defining Doctor Management Menu
def doctor_management_menu():
    print("Welcome to Doctor Management Window.......")
    d_df = pd.read_csv(d_path)
    print("1.Show Doctors\n2.Add new Doctor\n3.Delete Doctor Record\n4.Update Doctor Record")
    choice=int(input("Enter your Choice: "))
    if choice==1:
        print(d_df)
    elif choice==2:
        d_id=d_df["Doctor_ID"].count()+1
        name=input("Enter Doctor Name: ")
        cateogry=input("Cateogry of Doctor: ")
        fees=input("Enter Appointment fees of doctor: ")
        n=d_df["Doctor_ID"].count()
        d_df.loc[n]=[d_id,"Dr."+name.title(),cateogry,fees]
        d_df.to_csv(d_path,index=False)
        print("Doctor ID assigned: ",d_id)
        print("Dr."+name.title(),"has been added successfully.......")
    elif choice==3:
        print(d_df)
        d_id=int(input("Enter ID of Doctor whom you want to remove: "))
        confirm = input("Are you sure to delete above record: (y/n): ")
        if confirm == "y":
            d_df = d_df.drop(d_df[d_df["Doctor_ID"] == d_id].index)
            d_df.to_csv(d_path, index=False)
            print("Doctor removed successfully.....")
        elif confirm == "n":
            print("Doctor record is NOT deleted.....")
        else:
            print("Invalid Input...\nTry Again..")
    elif choice==4:
        print(d_df)
        which = int(input("Which record you want to update....\nEnter the Doctor Id associated with that record: "))
        df = d_df.loc[d_df["Doctor_ID"] == which]
        if df.empty:
            print("No such Doctor found....")
            doctor_management_menu()
        else:
            field = int(input('Which field you want to update...\n1.Doctor_Name\n2.Cateogry\n3.Appointment Fees\nEnter your Choice: '))
            if field == 1:
                name = input("Enter new Name: ")
                d_df.iat[which - 1, 1] = "Dr."+name
                d_df.to_csv(d_path, index=False)
                print(d_df.loc[d_df["P_ID"]==which])
                print("Record Updated successfully.....")
            elif field == 2:
                Cateogry = input("Enter Cateogry: ")
                d_df.iat[which - 1, 2] = Cateogry
                d_df.to_csv(d_path, index=False)
                print(d_df.loc[d_df["P_ID"]==which])
                print("Record Updated successfully.....")
            elif field == 3:
                fees = input("Enter new Appointment fees: ")
                d_df.iat[which - 1, 3] = fees
                d_df.to_csv(d_path, index=False)
                print(d_df.loc[d_df["P_ID"]==which])
                print("Record Updated successfully.....")

#Defining appointment Menu
def appointment_menu():
    a_df=pd.read_csv(a_path)
    print("Welcome to Appointment Scheduling Window.......")
    choice=int(input("1.Take Appointment\n2.Check Appointments\n3.Change Appointment Date\n4.Cancel Appointment\n5.Go Back\nEnter your Choice: "))
    if choice==1:
        add_appointment()
    elif choice==2:
        print(a_df)
    elif choice==3:
        p_id=int(input("Enter Patient ID: "))
        df=a_df.loc[a_df["P_ID"]==p_id]
        if df.empty:
            print("No suck Patient is found......")
        else:
            df = a_df.loc[a_df["P_ID"] == p_id]
            print(df)
            choice = input("Are you sure to change the appointment date of above Patient{y/n)?: ")
            if choice == "y":
                date = input("Enter new Appointment Date: ")
                a_df.iat[p_id - 1, 4] = date
                a_df.to_csv(a_path,index=False)
                print("Appointment date has been change successfully.\nYour new Appointment Date is",date)
            elif choice=="n":
                print("Okk....Appointment date is NOT changed...")
            else:
                print("Invalid input")
                return
    elif choice==4:
        p_id=int(input("Which Appointment do you want to cancel?\nEnter Patient ID associated with that: "))
        df = a_df.loc[a_df["P_ID"] == p_id]
        print(df)
        choice = input("Are you sure to cancel the appointment of above Patient(y/n)?: ")
        if choice == "y":
            a_df = a_df.drop(a_df[a_df["P_ID"] == p_id].index)
            a_df.to_csv(a_path, index=False)
            print("Appointment has been cancelled successfully....")
        elif choice == "n":
            print("Okk....Appointment is NOT cancelled")
        else:
            print("Invalid input")
            return
    elif choice==5:
        main_menu()
    else:
        print("Invalid Input....")
        print("Try Again..")
        appointment_menu()

#Function to add appointment
def add_appointment():
    p_df=pd.read_csv(p_path)
    a_df=pd.read_csv(a_path)
    choice = int(input("1.If Patient already registered\n2.If Patient NOT registerd\nEnter your choice: "))
    if choice == 1:
        p_id=int(input("Enter Patient ID: "))
        df=p_df.loc[p_df["P_ID"]==p_id]
        if df.empty:
            print("No such Patient is registered.....")
            print("Register the Patient first....")
            choice = (input("Would you like to Register(y/n)?"))
            if choice == "y":
                register_new_patient()
            elif choice =="n":
                print("GoodBye.....")
            else:
                print("Invalid input....")
                return
        else:
            check=a_df.loc[a_df["P_ID"]==p_id]
            if check.empty:
                p_name = p_df.iat[p_id - 1, 1]
                df = p_df.loc[p_df["P_ID"] == p_id]
                print("Selected Patient details:\n ", df)
                print("List of doctors is below.....")
                d_df = pd.read_csv(d_path)
                print(d_df)
                choice = int(input("Enter ID of the Doctor you want Appointment with: "))
                date = input("Enter date for your Appointment(DD-MM-YY): ")
                d_name = d_df.iat[choice - 1, 1]
                d_cat = d_df.iat[choice - 1, 2]
                print("Your Appointment with", d_name, "(", d_cat,
                      ") has been fixed.........\nYour date of Appointment is :", date)
                a_df = pd.read_csv(a_path)
                n = a_df["P_ID"].count()
                a_df.loc[n] = [p_id, p_name.title(), d_name, d_cat, date]
                a_df.to_csv(a_path, index=False)
                print(a_df.loc[a_df["P_ID"]==p_id])
            else:
                print("Patient ID",p_id,"has already taken appointment.\nAppointment details of the given Patient: \n",check)


    elif choice==2:
        print("Register the Patient first....")
        choice = (input("Would you like to Register(y/n)?"))
        if choice == "y":
            register_new_patient()
        elif choice == "n":
            print("Appointment can not be done , without registration.....\nGood Bye")
        else:
            print("Invalid input....")
            add_appointment()
            return

#Defining Reports Menu
def reports_menu():
    print("Welcome to Reports and Analysis Window.......")
    p_df = pd.read_csv(p_path)
    a_df=pd.read_csv(a_path)
    r_df=pd.read_csv(r_path)
    choice=int(input("1.Create Report\n2.Show all Reports\n3.Update Report\n4.Go Back\nEnter your choice: "))
    if choice==1:
        print(p_df)
        p_id=int(input("Whose report you want to create?\nEnter the Patient ID: "))
        df=r_df.loc[r_df["P_ID"]==p_id]
        if df.empty:
            p_name = p_df.iat[p_id - 1, 1]
            disease = input("Patient is affected by: ")
            Treatment = input('Treatment provided to patient: ')
            status = input("Enter Status of Patient: ")
            n = r_df["P_ID"].count()
            r_df.loc[n] = [p_id, p_name, disease, Treatment, status]
            r_df.to_csv(r_path, index=False)
            print(r_df.loc[r_df["P_ID"]==p_id])
            print("Report added successfully.......")
        else:
            print("Report of Patient with Patient ID",p_id," is already created......")
            print(r_df)

    elif choice==2:
        print(r_df)
    elif choice==3:
        p_id=int(input("Whose Report you want to update?\nEnter Patient ID: "))
        df = r_df.loc[r_df["P_ID"] == p_id]
        if df.empty:
            print("There is no such Patient ID....")
        else:
            field = int(input("Which field do you want to update?\n1.Disease/injury\n2.Treatment\n3.Status\nEnter your choice: "))
            if field == 1:
                disease = input("Patient is affected by which disease/injury: ")
                r_df.iat[p_id - 1, 2] = disease
                r_df.to_csv(r_path, index=False)
                print(r_df.loc[r_df["P_ID"]==p_id])
                print("Report updated successfully...")
            elif field == 2:
                Treatment = input("Treatment provided to Patient: ")
                r_df.iat[p_id - 1, 3] = Treatment
                r_df.to_csv(r_path, index=False)
                print(r_df.loc[r_df["P_ID"]==p_id])
                print("Report updated successfully...")
            elif field == 3:
                Status = input("Enter Status of Patient: ")
                r_df.iat[p_id - 1, 4] = Status
                r_df.to_csv(r_path, index=False)
                print(r_df.loc[r_df["P_ID"]==p_id])
                print("Report updated successfully...")
    elif choice==4:
        main_menu()
    else:
        print("Invalid Input")

main_menu()