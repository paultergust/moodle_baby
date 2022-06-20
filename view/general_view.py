# TEMP VIEW

class GeneralView():

    def display_menu(self, options, input_display="Select an option: "):
        for k in options:
            print(k)
        r = input(input_display)
        return r.strip().casefold()
    
    def display_list(self, l):
        print(l)
    
    def display_error(self, msg):
        print(f'Warning: {msg}')