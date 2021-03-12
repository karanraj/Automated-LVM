import subprocess as sp
import os

def PV():
    while 1:
        os.system("clear")
        os.system("tput setaf 6")
        os.system("figlet -tkc -f small -w 80 Physical Volume")
        os.system("tput setaf 7")
        print("""
        1. Create PV
        2. Delete PV
        3. Display PV
        p. Go Back
        q. Exit
        """)
        n=input("Enter your choice: ")
        if n=='1':
            disk=input("Enter disk or parttion: ")
            out=sp.getstatusoutput("echo y | pvcreate " + disk)
            if out[0]==0:
                os.system("tput setaf 2")
                print("PV Created Successfully")
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")
        
        if n=='2':
            disk=input("Enter disk or parttion: ")
            out=sp.getstatusoutput("pvremove -f " + disk)
            if out[0]==0:
                os.system("tput setaf 2")
                print("PV Deleted Successfully")
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")
    
        elif n=='3':
            out=sp.getstatusoutput("pvdisplay ")
            if out[0]==0:
                os.system("tput setaf 2")
                print(out[1])
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        elif n=='p':
            break
        elif n=='q':
            exit()
            
def VG():
    while 1:
        os.system("clear")
        os.system("tput setaf 6")
        os.system("figlet -tkc -f small -w 80 Volume Group")
        os.system("tput setaf 7")
        print("""
        1. Create VG
        2. Delete VG
        3. Display VG
        p. Go Back
        q. Exit
        """)
        n=input("Enter your choice: ")
        if n=='1':
            vg_name=input("Enter VG name: ")
            pv=input("Enter PV name: ")
            out=sp.getstatusoutput("vgcreate " + vg_name + ' ' + pv)
            if out[0]==0:
                os.system("tput setaf 2")
                print("VG Created Successfully")
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        if n=='2':
            vg_name=input("Enter VG Name: ")
            out=sp.getstatusoutput("vgremove -f " + vg_name)
            if out[0]==0:
                os.system("tput setaf 2")
                print("VG Deleted Successfully")
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        elif n=='3':
            out=sp.getstatusoutput("vgdisplay ")
            if out[0]==0:
                os.system("tput setaf 2")
                print(out[1])
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        elif n=='p':
            break
        elif n=='q':
            exit()

def LV():
    while 1:
        os.system("clear")
        os.system("tput setaf 6")
        os.system("figlet -tkc -f small -w 80 Logical Volume")
        os.system("tput setaf 7")
        print("""
        1. Create LV
        2. Delete LV
        3. Display LV
        4. Mount LV
        5. Extend LV
        6. Reduce LV
        p. Go back
        q. Quit
        """)
        n=input("Enter your choice: ")
        if n=='1':
            lv_name=input("Enter LV Name: ")
            lv_size=input("Enter size of LV: ")
            vg_name=input("Enter VG name: ")
            lvc=sp.getstatusoutput("lvcreate --size  " + lv_size + " --name " + lv_name + " " + vg_name)
            lvf=sp.getstatusoutput("mkfs.ext4 /dev/" + vg_name + "/" + lv_name)
            if lvf[0]==0:
                os.system("tput setaf 2")
                print("LV Created and Formated Successfully")
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(lvc[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        elif n=='2':
            lv_name=input("Enter Name: ")    
            out=sp.getstatusoutput("lvremove -f " + lv_name)
            if out[0]==0:
                os.system("tput setaf 2")
                print("LV Deleted Successfully")
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        elif n=='3':
            out=sp.getstatusoutput("lvdisplay")
            if out[0]==0:
                os.system("tput setaf 2")
                print(out[1])
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        elif n=='4':
            folder=input("Enter Destination: ")
            drive=input("Enter Source: ")
            out=sp.getstatusoutput("mount " + drive + " " + folder)
            if out[0]==0:
                os.system("tput setaf 2")
                print(drive+ " Mounted Successfully to " + folder)
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        elif n=='5':
            drive=input("Enter LV: ")
            size=input("Enter size to extend: ")
            out=sp.getstatusoutput("lvextend --size +" + size + " " + drive)
            e2=sp.getstatusoutput("e2fsck -p " + drive)
            resize=sp.getstatusoutput("echo y | resize2fs " + drive)
            if out[0]==0:
                os.system("tput setaf 2")
                print(drive + "Extnded Successfully")
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        elif n=='6':
            drive=input("Enter LV: ")
            size=input("Enter size to reduce: ")
            os.system("umount " + drive)
            e2=sp.getstatusoutput("e2fsck -p " + drive)
            resize=sp.getstatusoutput("echo y | resize2fs " + drive + " " + size)
            out=sp.getstatusoutput("echo y | lvreduce --size -" + size + " " + drive)
            if out[0]==0:
                os.system("tput setaf 2")
                print(drive + "Reduced Successfully")
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print(out[1])
                os.system("tput setaf 7")
            input("Press enter key to continue...")

        elif n=='p':
            break
        elif n=='q':
            exit()

while 1:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -tkc -f small -w 80 LVM")
    os.system("tput setaf 7")
    print("""
    1. Physical Volume
    2. Volume Group
    3. Logical Volume
    q. Quit
    """)
    n=input("Enter your choice: ")
    if n=="1":
        PV()
    elif n=='2':
        VG()
    elif n=='3':
        LV()

    elif n=='q':
        exit()
