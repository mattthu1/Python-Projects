#create definitions for conditions within the program
class Smartphone:
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.name = name
        self.apps = {}
        self.report()

#adds new apps to the smartphone

    def add_app(self, appname, appsize):

        if appname in self.apps:

            print(f"App '{appname}' is already installed.")
            return
        
        if self.get_available_space() < appsize:
            print("Cannot install app, no available space.")
            return
        
        self.apps[appname] = appsize
        
        
#remove apps from the smartphone

    def remove_app(self, appname):

        if appname in self.apps:

            appsize = self.apps.pop(appname)

            print(f"App '{appname}' has been removed.")
            
        else:
            print(f"App '{appname}' is not installed.")

# checkss if app is installed on the smartphone

    def has_app(self, appname):
        return appname in self.apps

    def get_available_space(self):
        return self.capacity - sum(self.apps.values())

#prints a detailed report of the smartphone's information

    def report(self):
        print(f"Name: {self.name}")
        print(f"Capacity: {sum(self.apps.values())} out of {self.capacity} GB")
        print(f"Available space: {self.get_available_space()}")
        print(f"Apps installed: {len(self.apps)}")
        for app, size in sorted(self.apps.items()):
            print(f"* {app} is using {size} GB")

#actually asking the user what they want to do with the smartphone

def main():
    size = int(input("Size of your new smartphone (32, 64 or 128 GB): "))
    name = input("Smartphone name: ")
    print('Smartphone created!')

    phone = Smartphone(size, name)
    while True:
        print("(r)eport, (a)dd app, r(e)move app or (q)uit:")
        choice = input().lower()
        if choice == "r":
            phone.report()
        elif choice == "a":
            appname = input("App name to add: ")
            appsize = int(input("App size in GB: "))
            phone.add_app(appname, appsize)
        elif choice == "e":
            appname = input("App name to remove: ")
            phone.remove_app(appname)
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
