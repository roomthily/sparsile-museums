import requests

'''
handlers for the museum apis

currently supports:
    cooper hewitt
'''


class Museum(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def search(self, **kwargs):
        '''
        '''
        pass

    def parse(self, output):
        '''
        '''
        pass

    def _get(self, url):
        data = {}
        try:
            rsp = requests.get(url)
            if rsp.status_code >= 300:
                return data

            data = rsp.json()
        except:
            pass

        return data


class CooperHewitt(Museum):
    '''
    https://api.collection.cooperhewitt.org/rest/?method=cooperhewitt.search.objects
        &access_token=A_TOKEN&color=00ff00
        &has_images=1&page=1&per_page=100

    note: not sure about the has_images value, but it is the only
          on tried that returned results if has_images included

    anyway.

    the base_url = https://api.collection.cooperhewitt.org/rest/
    '''
    def search(self, **kwargs):
        '''
        for cooper, we need the access token, color (a hex color),
            has_images of 1, page (1), per_page (100), and the search method
            (method=cooperhewitt.search.objects)

        NOTE: the hex string must start with &#35; and must include the hash.
              if you don't include the hash at all, it really fails
              that color match

        NOTE: we don't really need many of the objects, so the
              per_page default will be like 5

        '''

        pass

    def parse(self, output):
        '''
        output is the json body of the search results
        '''
        # TODO: grab a random one?
        the_obj = iter(next(output.get('objects', [])), None)
        if not the_obj:
            return {}

        obj_title = the_obj.get('title', 'Not Available')
        obj_url = the_obj.get('url', '')
        obj_credit = the_obj.get('creditline', 'Not Available')

        image = iter(next(the_obj.get('images', [])), None)
        if not image:
            # TODO: send an error image instead?
            pass

        return {
            "title": obj_title,
            "url": obj_url,
            "credit": obj_credit,
            "image_url": image.get("z", {}).get("url", ""),
            "image_width": image.get("z", {}).get("width", ""),
            "image_height": image.get("z", {}).get("height", "")
        }
