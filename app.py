from flask import Flask, render_template, request, redirect, session, url_for
from py import *
import json

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)
env.globals.update(helpers=helpers)

@app.route('/map')
@app.route('/map/<type>')
def map(type=''):
	return google_maps.map(type)

@app.route("/", methods = ["GET","POST"])
def index():
    print 'on index page'
    if request.method == "GET":
        print 'get'
        return render_template("index.html")
    else:
        print 'post'
        button = request.form['button']
        print 'after button'
        if button == "Submit":
            print 'right before'
            session['latitude'] = request.form.get('latitude', None)
            session['longitude'] = request.form.get('longitude', None)
            print session['latitude']
            print session['longitude']
            unicodeobj = request.values.getlist("tour")
            var = []
            for iterating_var in unicodeobj:
                print ' hello'
                iterating_var = iterating_var.encode ('ascii', 'ignore')
                var.append(iterating_var)
            print var
            session ['var'] = var
            session['page'] = 'makeTour'
            return redirect(url_for('makeTour'))

@app.route ("/makeTour",  methods = ["GET","POST"])
def makeTour():
    if 'page' in session.keys() and session['page'] == 'makeTour':
    	#locs = [['Battery Park', 'New York', '4.2', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=768&photoreference=CnRpAAAAMmvLcY5d9jSdJfWIAwNQqjannSLcoIfUeEHmbMr3NnPqW6Zfm56FAkP9lrvTbGxEroxcmXwu1iLUVl8_USVoMTs37uimoUXRhtZiF9rQBBgUVj9azSpGTGHCRTDBnhMUsx-0S3kBKsxjjSp7gQZjXhIQnsjprXeDVp37TBlE7TI1dBoUIn28jXHarzQV4EIsix4or7Gsmok&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['9/11 Memorial', '1 Albany Street, New York', '4.4', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=816&photoreference=CnRoAAAAJKg4_Q_nV5iMPaCS-zKEPVYfv47_5_goUDZKIoRZEbHkijr_HrPRMi7ZXujAwTvD7eTrbdruAtivVe-iwaYgqdeFzlhnRaFSqD3MJU_HMP9r2R0uewrekwNz8-ZiqObIZGzaHEWb--ARwfS4__pUYxIQstChGTJVBS1Ax2AZ45DoaBoUyfzFNEBR6Rcb6ELvx565cYKYYx8&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['City Hall Park', 'Broadway, Manhattan', '4.2', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=250&photoreference=CpQBhQAAAEIWbMyKl9vOCVcMWrbNpAyE9tXeXQLxLZLZnA5EWEcrwahPxwD1gVXFsLmDwiD2AL1B_lYULBfYXI6TwJUILHyogjFUgCSgJiMYkuW9j4NBAMwPLwLH7ExwH2R-qaWyVilVT1SKvPnAL8cLdIPPXf-TenU495C-WHHvrk9_wXjef6WMh5mu9KdbC-8FTVhEvBIQLFgwwl4e6BZ0j431zsSMWBoUzB0xAdbtLqeZg3BUfPRlDt13b1k&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Brooklyn Bridge Park', '334 Furman Street, New York', '4.5', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1152&photoreference=CpQBhgAAAKFEsaDUDdCxLsEgOfYl0tSZsOWo5s93HTlM1RDHWybq-WrrjW-86yhT-nBQTTwv6ofFIB7vNax-aI6Hvmbezk3OoTr9nVbe0F9NI7rpvIKN1GwQJRoiJwzUzMxPGc-FKnzYZyNMvgdgEEa-VvHTFDZV_KylTWoYAdczhRMMOx-iI6jvlFLHKqLpcPpGjJmZ_xIQ2zxrg000FLdJiB4IpP-jEBoUJ3WI6O7tO2S0bvjw7FgTROJVnVQ&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Tompkins Square Park', '500 East 9th Street, New York', '3.8', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1224&photoreference=CoQBdgAAAHNLDSYhjJeOb1Ta1tKRs2aXcCQXijtGfkTtIjsh4DK7i1T0Ii5ytdhHMzuqvOkaaANpTZr6TPiWa_734feIcHE7sCDubHpKhZumSGm2DMKLZKv5dwCQVWDKax4xaYp219zXvGfoIB7PRH9zajkxGBD80LXosiapPEb2jBozH4s9EhC2_PtMU6yhMYsdKZ6gZSDFGhTLNrMMwNu_8-sVST3hU7GzRPcBMw&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Washington Square Park', '5 Ave, New York', '4.3', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference=CqQBlgAAAE-eRFsVVaDuw_wewvN-UJGCwUVfk9jlIjTlOm1n-N-sFoibYJW9_Nqe31MYDSZiVFkeotnjeDWy1CRHV2BPihmf1e1qGFxwNnzx1K0vgbON4-dKJgXOEsGNppUwMe28FnlXnA8po9i1PGhXvOmBPQ36RFdnIw1GWgTCAE9PASyEmXN_ZxETeVrmJ6ddO4l1TFNhzeIk5d709S4kxqfBwUESEHCkBlLLnjbO1VDxD0SfPSsaFOqajkwSKKwj7kD36tuvNp5yxP1T&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Liberty State Park', '200 Morris Pesin Drive, Jersey City', '4.3', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1251&photoreference=CnRnAAAA0o2Y6usxPuhal6WeHCmy0ywNpbRoepoR622qhz8zphEtUFcHaygS0PkpLh2oNmgdbccKWn_6NxSpEGuSqGpTDy8nc-2oKirPTE2qz48fK9_7lRrZX3mEqakdCNTU30R3MqfhZZU2r0BiiSnReFIaPxIQz8w2iPLEtKXPmrWzQMtnnxoUeRkRJ6x0bG9ej0RsrxsJIkakISg&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['East River Park', 'East River Promenade, New York', '4.6', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1632&photoreference=CoQBcQAAACr1nGkUJv26zZePyKnOi6X-iPoK3lWHs5Hdkus5TwnoTTNl1RqOBohT3rgMYsSQzyxQjgCdED0Nc7chfXdcQ37G7yLTY6Qhy7XsiS_5JzGRoacwWcRf3H-gYuPvaU9jjGInJgkDFSVc-pHJUc4w_XJoov5cxq2fruR_aJAelyHIEhAofQaHxq4rseodPescT1xnGhQzXzHW2yc9_9-YCY_IjfCOPN_3Sw&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Madison Square Park', 'Madison Avenue, New York', '4.2', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1536&photoreference=CnRnAAAAIuXVU-pChPWExskC4zEh5UgnBy9dsYOuQuhvvVwkJ3zVgIRaIrQDZZpxHGYahK0bQroR5Q2qnLQyDyI5zEjXD_HZs7_JsiGjl08pdwqTsmEM8EOQUEndhnRLb9ERFZMPhHVP-mlFekvyXDoWGLaRWhIQqC07ykmks7dqgzMN4Bv_MxoUjM_wnVTHv16OxXaNcW7jcBdL36o&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Zuccotti Park', 'New York', '3.9', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1536&photoreference=CnRwAAAAG6LvvOiHuQk8ev1lbKKarDU9U0jXHeqSGaoMxZFImFDKCLoLPMi32DYwgpTIr0bxRC5l0NGQL53znAAJVrAu91FXyXO3xcWU_CdCN_rCGT7d3utT1hjnMwQDHIG25iaQXqOT5cCLGsR_ttJRneuctBIQFnnUqqhQ1tYxX43MQDmb7BoU2zSoHyhWt9p0kHkV67WnmU46yhw&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Fort Greene Park', 'Myrtle Avenue, Brooklyn', '4.3', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1632&photoreference=CoQBcgAAAFNAgW_qzjwq44TSH1wB_bXQlgRHsjmeh3OBv-35GZIjYPbr3Om6RWvUMg21m3hMz3SH-SJA7Cwlrgi5YZa2bw8BENRYMHNSp_Be6O9i7h99dABKsZhoyUa4khANPuDHcjsEaruR3f6zQY9Zgx2b5T2LQcLHF-7sj3Wt0J5nEC_NEhBuqGMHuIHElxQjHFrfzuFpGhTrEFUG9Fy6Ciz3906VwfmywJoXeQ&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Empire Fulton Ferry', 'Water Street, Brooklyn', '4.5', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=936&photoreference=CqQBmQAAAK4rMVy8d4vqy3gVLxdZFp9oRxho_3nU54mlQ6lyUjoSoFz4PfbBDOMJKoRNqz-EbmmDaQnBkcULfQzWNgn9adgansZXCWRRvFW__10wRhfdEynQN0l6udk2Y5BDEN4Z31VYGwRjcVrCKs_UIUiAJkVi-3jmtO8UqQ7KEvDrzeoA8GwYTGAyk1SfqJvBeVAxRgt8EgalERSXXon2WliKpVESEFYTGhZbc12_SIR4Xw0we-oaFIdiP9PosDoU-YN7I1xQhL_wFhm5&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Governors Island National Monument', 'United States', '4.5', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=648&photoreference=CnRoAAAAD8S7LNwlwBI8MZTuleyU3gk-iqkokYLd-9wwOed9atlkEcntLF1Z_9V1bl3S09VgJ3C6zr5L3wa6iSumV6CnNdeOdr5nJlLYVPWFQME4Hph8PHO7GzUyCpPAu4D6F78YBBshuxXtHfTHO8JCOI7WrRIQSmOORlvXGpXLl0adG5BTGhoUw2iw6Xve28E-cTdBKSFv0h1p3Wc&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['African Burial Ground National Monument', '290 Broadway, New York', '4', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=768&photoreference=CqQBkQAAAIVDwzXeT8wzPRYCKDiVb-HvLTPbKORT15Mjcd2WBaw1LlX6w8Fg3SB3Xvxl011fbbg6D_7zk8DyFoHVUav3PjWQIPJDoFeMKRfGhE6HZcNaaZcdg4DAzZuBy6grQMzNEy7mbUnmO95C5NZdjWhf-0lamAZ9Bpsi9bitfooR6TBmSs-w6-BYbdFTqsBJ6IrO6Gen4_rcE1XfeWcxmBaRYF4SEIWBmE5kBqgDqCaGgdHmXP0aFFaEKIPIWpWtTU890lkZfdM-2P2y&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Foley Square', '111 Worth Street #4g, New York', '4.4', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=2048&photoreference=CnRsAAAApN_ed0wnbb3NW6l87rf0UvpeQQ7gWwAG6YOG9ZohMbd78ll5IF9nGrl98uy8WR7hVUdH-UtxMWshp2nguHhBhMapPRFifOLIboaR-xuvUB7f0phau1jI3X-E_snBAmj3SZocWRhv1y6-rdM9OEzM6BIQxaXWL7ybljaesTprhPQ2KhoUcEQU2rgCLepQCWgu3ra10kpLHZg&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Sara D. Roosevelt Park', 'New York', '3.9', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=972&photoreference=CoQBegAAABvcPqaHIAWkNGauB6u-v5Pi0kU3Fqe4OCZMd5ggoge83oaeilb5ZqRu-poQpVFR3E51WLC6WFn_EO4KDNgYjqIF0HfDJMmPItzkaMSaQSit-3YtM1H6o6IoEpiXeA_D_JL9QgQbFlvivvYTvNCgIXZmSXFgeSq_c67Nhu2kyJ51EhDtB_em9skXjAbfywjDFR9hGhQhKSQTXRx1t4H6jeWpGG4L8IH1Mg&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Bowling Green', 'Broadway & Whitehall St., New York', '4.3', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=2048&photoreference=CoQBegAAAHnRFElrCAUf88F2iXKgjzTp0vsuKOo-9kXHiPxvmRRxOusweOElutVC67KXBWBGD-2mlRyZDwe0fVOmVFdRdd9GVD1_MCr1_auByaqSKVJDkvbKfNJ0jJ9cqQ-vjkJI4uFrioKaKwg8H86-4wpEuAQ4AGcziTqGRGnRK3GwWLUbEhAEayRHX23azkScmzDlcntdGhQL-mgSoBlSe153GAuygjncNJOH2A&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Hudson River Park', 'New York', '4.4', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1632&photoreference=CnRoAAAAMce476MNQTbA8UBieMnwWLYBRG94GAygKcf8RQbUGPjZAe9w5V6fgJeu7jbgbGCbhK0zPR_RkAfAPvaXnDvbkyEK24497lir-tbo2QTezbVgngeRNQ2s84h72ipGIc2gz4HOE1gs8E8nZDcSCZHkGxIQVq4GwddBc9mToxLS_z7qyBoUfBXBxV4zWwIAv5EQ_dMhGc8bOx4&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Irish Hunger Memorial', 'Vesey Street, New York', '4.8', u'https://maps.googleapis.com/maps/api/place/photo?maxwidth=864&photoreference=CnRoAAAAHH8C-dSd-eZqMnSJC5laYTwZoQRnQiubHJty-Mze2T_ytorb0iGITbnGZBvdzBIVoOj00U92-IMli0iSV_FsUAkOCuwPGSvPpz6UXIvFgeN-5m7bwuKiS3Zq5uoNCPNmorHnqT7XMrUdDnhdCkwKdhIQAeYRXVJghGvlLY7K_mhRzxoUIwv1xX7lKaVUNcuaaHAw3U7GYIE&sensor=true&key=AIzaSyB_UESBeiHoBu4tMSfT2yrjLjTzMSa6ruw'], ['Hamilton Fish Park', '128 Pitt Street, New York', '3.8', 'http://www.profyling.com/wp-content/uploads/2012/08/no-image-available.jpg']]
        var  = session['var']
        longitude = session['longitude']
        latitude = session['latitude']
        locs = google_places.findPlaces(latitude, longitude, var)
        if request.method =="GET":
            return render_template("make_tour.html",locs=locs)
        else:
            button = request.form['button']
            if button == "Submit":
                print "hello"
                unicodeobj = request.values.getlist("place")
                var = []
                for iterating_var in unicodeobj:
                    iterating_var = iterating_var.encode ('ascii', 'ignore')
                    var.append(iterating_var)
                var = google_directions.get_waypoint_order(latitude+","+longitude,var,latitude+','+longitude)
                session['waypoints'] = var
                session['page'] = 'showDirections'
                return redirect(url_for("showDirections"))
    else:
        return redirect('/')



@app.route("/showDirections")
def showDirections():
    if 'page' in session.keys() and session['page'] == 'showDirections':
        waylist = session['waypoints']
        endpoint = waylist.pop()
        waylist = citi_bike.make_location_array(session['latitude'],session['longitude'],session['latitude'], session['longitude'], waylist)
        waypoints = []
        baseLoc = session['latitude'] + "," + session['longitude']
        for waypoint in waylist:
            waypoints.append({"location":waypoint.encode('ascii', 'ignore')})
        print "OUTPUT:" + str(waypoints)
        result = dict()
        result['start'] = baseLoc
        result['end'] = endpoint
        result['waypoints'] = json.dumps(waypoints)
        session['page'] = ''
        return render_template("show_directions.html", result = result)
    else:
        return redirect("/")


@app.route("/updatedata")
def updateData():
    utils.update_citi_bike_stations()
    return redirect("/")

@app.errorhandler(404)
def error404(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
	return render_template("errors/500.html"), 500

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5007)
