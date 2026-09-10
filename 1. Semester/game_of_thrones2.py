name = input("Name: ")

match name:
    case "Jaime" | "Cersei" | "Tyrion":
        print("Lannister")
    case "Arya" | "Sansa":
        print("Stark")
    case "Daenerys":
        print("Targaryen")
    case _:
        print("Wer?")