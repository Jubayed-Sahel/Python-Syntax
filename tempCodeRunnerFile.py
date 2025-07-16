str1 = str(input()) 
str2 = str(input())
str3 = str(input())


match str1:
    case 'vertebrado':
        match str2:
            case 'ave':
                match str3:
                    case 'onivoro':
                        print("pomba")
                    case 'carnivoro':
                        print("aguia")
            case 'mamifero':
                match str3:
                    case 'onivoro':
                        print("homem")
                    case 'herbivoro':
                        print("vaca")
    case "invertebrado":
        match str2:
            case 'inseto':
                match str3:
                    case 'hematofago':
                        print("pulga")
                    case 'herbivoro':
                        print("lagarta")
            case 'anelideo':
                match str3:
                    case 'hematofago':
                        print("sanguessuga")
                    case 'onivoro':
                        print('minhoca')        
                