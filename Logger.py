import speedtest
import requests


class Logger:
    # (14237) Frontier (Miami, FL, United States) [2201.71 km]
    server = [14237]
    url = 'https://mf.us4.hqrentals.app/form/6ebe1465-ba37-46e9-86d6-f0764e9127f5'
    results = {
        'download': '',
        'upload': '',
        'ping': '',
        'timestamp': '',
        'bytes_sent': 0,
        'bytes_received': 0,
        'share': '',
        'server': {
            'url': '',
            'lat': '',
            'lon': '',
            'name': '',
            'country': '',
            'sponsor': '',
            'id': '',
            'host': '',
            'd': 0,
            'latency': 0
        },
        'client': {
            'ip': '',
            'lat': '',
            'lon': '',
            'isp': '',
            'isprating': '',
            'rating': '',
            'ispdlavg': '',
            'ispulavg': '',
            'loggedin': '',
            'country': ''
        }
    }
    payload = {
        'field_273': '',
        'field_275': '',
        'field_287': '',
        'field_292': '',
        'field_281': '',
        'field_272': '',
        'field_270': '',
        'field_279': '',
        'field_278': '',
        'field_296': '',
        'field_297': '',
        'field_300': '',
        'field_301': '',
        'field_293': '',
        'field_286': '',
        'field_284': '',
        'field_299': '',
        'field_298': '',
        'field_282': '',
        'field_294': '',
        'field_283': '',
        'field_274': '',
        'field_295': '',
        'field_276': '',
        'field_285': '',
        'field_271': '',
        'field_280': '',
    }

    def logAndSave(self):
        self.log()
        self.save()

    def save(self):
        data = self.log()
        self.setResponse(data)
        self.setPayload()
        self.sendData()
        print('process completed')

    def setPayload(self):
        self.payload = {
            'field_273': self.results['bytes_received'],
            'field_275': self.results['bytes_sent'],
            'field_287': self.results['server']['country'],
            'field_292': self.results['client']['country'],
            'field_281': self.results['server']['d'],
            'field_272': self.results['timestamp'],
            'field_270': round(self.results['download'] / 1000000, 2),
            'field_279': self.results['server']['host'],
            'field_278': self.results['server']['id'],
            'field_296': self.results['client']['ip'],
            'field_297': self.results['client']['isp'],
            'field_300': self.results['client']['ispdlavg'],
            'field_301': self.results['client']['isprating'],
            'field_293': self.results['client']['ispulavg'],
            'field_286': self.results['server']['latency'],
            'field_284': self.results['server']['lat'],
            'field_299': self.results['client']['lat'],
            'field_298': self.results['client']['loggedin'],
            'field_282': self.results['server']['lon'],
            'field_294': self.results['client']['lon'],
            'field_283': self.results['server']['name'],
            'field_274': self.results['ping'],
            'field_295': self.results['client']['rating'],
            'field_276': self.results['share'],
            'field_285': self.results['server']['sponsor'],
            'field_271': round(self.results['upload'] / 1000000, 2),
            'field_280': self.results['server']['url'],
        }

    def sendData(self):
        r = requests.post(self.url, self.payload)

    def setResponse(self, data):
        self.results = {
            'download': data['download'],
            'upload': data['upload'],
            'ping': data['ping'],
            'timestamp': data['timestamp'],
            'bytes_sent': data['bytes_sent'],
            'bytes_received': data['bytes_received'],
            'share': data['share'],
            'server': {
                'url': data['server']['url'],
                'lat': data['server']['lat'],
                'lon': data['server']['lon'],
                'name': data['server']['name'],
                'country': data['server']['country'],
                'sponsor': data['server']['sponsor'],
                'id': data['server']['id'],
                'host': data['server']['host'],
                'd': data['server']['d'],
                'latency': data['server']['latency']
            },
            'client': {
                'ip': data['client']['ip'],
                'lat': data['client']['lat'],
                'lon': data['client']['lon'],
                'isp': data['client']['isp'],
                'isprating': data['client']['isprating'],
                'rating': data['client']['rating'],
                'ispdlavg': data['client']['ispdlavg'],
                'ispulavg': data['client']['ispulavg'],
                'loggedin': data['client']['loggedin'],
                'country': data['client']['country']
            }
        }

    def log(self):
        # If you want to test against a specific server
        # servers = [1234]
        threads = None
        # If you want to use a single threaded test
        # threads = 1
        s = speedtest.Speedtest()
        s.get_servers(self.server)
        s.get_best_server()
        s.download(threads=threads)
        s.upload(threads=threads)
        s.results.share()
        return s.results.dict()
