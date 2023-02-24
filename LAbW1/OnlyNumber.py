
def notnumrestrict(entry,top):

    def correct(inp):
        if inp.isdigit() and len(inp) < 5:
            return True
        elif inp == "":
            return True
        else:
            return False
    reg = top.register(correct)
    entry.config(validate='key',validatecommand=(reg,'%P'))
    