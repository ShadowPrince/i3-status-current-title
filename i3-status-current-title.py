import i3
import time

MAX_WIDTH = 80
CACHED_TIME = 0.5

def find_focused(tree):
    if type(tree) == list:
        for el in tree:
            res = find_focused(el)
            if res:
                return res

    elif type(tree) == dict:
        if tree["focused"]:
            return tree
        else:
            return find_focused(tree["nodes"] + tree["floating_nodes"])

class Py3status:
    def currentTitle(self, json, i3status_config):
        response = {'full_text': '', 'name': 'current-title', 'cached_until': time.time() + CACHED_TIME}

        try:
            window = find_focused(i3.get_tree())

            if window and "name" in window:
                response["full_text"] = len(window["name"]) > MAX_WIDTH and "..." + window["name"][-MAX_WIDTH:] or window["name"]

            # There is such encode in py3status, if it fails plugin will shutdown
            response['full_text'].encode('utf-8')
        except:
            pass

        return (0, response)
