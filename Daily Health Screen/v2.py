from threading import Timer
import webbrowser


def do_health_screen(symptoms: bool = False, explainable: bool = False) -> None:
    """
    Fills Out The RIT Daily Health Screen, Hooks Included For Customization / Potential Discord Bot ?

    :param symptoms: First.txt Yes/No on DHS, Do You Have Symptoms?
    :param explainable: If Yes on The Above, Are They Explainable As Something Other Than Covid
    """

    # Are You Getting Sent To The Shadow Realm ?
    in_danger_zone = True if symptoms and not explainable else False

    site = webbrowser.open("https://dailyhealth.rit.edu/login.html")


    return None


def run_continuously():
    Timer(interval=86400, function=run_continuously)
    do_health_screen()


