import json

from flask import Flask, request, render_template, redirect, url_for, make_response
from flask import jsonify
from flask import Response
import time
import re

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

def s1(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return_dict = {
        "name": username,
        "time": now
    }
    if re.match(r'[a-mA-M]', username[0]):
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)  
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')   
            
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response


def s2(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if re.match(r'[a-mA-M]', username[0]):
        return_dict = {
            "name": username,
            "time": now
        }
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        return_dict = {
            "name": username,
            "time": now
        }

        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response


def s3(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if re.match(r'[a-mA-M]', username[0]):
        return_dict = {
            "name": username,
            "time": now
        }
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        return_dict = {
            "name": username,
            "time": now
        }

        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response


def s4(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if re.match(r'[a-mA-M]', username[0]):
        return_dict = {
            "name": username,
            "time": now
        }
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        return_dict = {
            "name": username,
            "time": now
        }

        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response


def s5(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if re.match(r'[a-mA-M]', username[0]):
        return_dict = {
            "name": username,
            "time": now
        }
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        return_dict = {
            "name": username,
            "time": now
        }

        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response


def s6(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if re.match(r'[a-mA-M]', username[0]):
        return_dict = {
            "name": username,
            "time": now
        }
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        return_dict = {
            "name": username,
            "time": now
        }

        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response


def s7(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if re.match(r'[a-mA-M]', username[0]):
        return_dict = {
            "name": username,
            "time": now
        }
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        return_dict = {
            "name": username,
            "time": now
        }

        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response


def s8(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if re.match(r'[a-mA-M]', username[0]):
        return_dict = {
            "name": username,
            "time": now
        }
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        return_dict = {
            "name": username,
            "time": now
        }

        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response


def s9(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if re.match(r'[a-mA-M]', username[0]):
        return_dict = {
            "name": username,
            "time": now
        }
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        return_dict = {
            "name": username,
            "time": now
        }

        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response


def s10(username, map_dict):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if re.match(r'[a-mA-M]', username[0]):
        return_dict = {
            "name": username,
            "time": now
        }
        response = make_response(jsonify(return_dict))
        next_invoke = map_dict.get('json', '')
    else:
        return_dict = {
            "name": username,
            "time": now
        }

        xml = []
        for k in return_dict.keys():
            v = return_dict.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
            xml.append('\n')
        response = Response(response='<xml>\n{}</xml>'.format(''.join(xml)), status=200, mimetype="application/xml")
        response.headers["Content-Type"] = "text/xml; charset=utf-8"
        next_invoke = map_dict.get('xml', '')
    response.set_cookie(key='next', value=next_invoke)
    return response



def get_map(file_name):
    '''
    :param file_name: invoke_logic.txt
    :return: invoke_logic_map
    like  => 
        {
            's1': {'this': s1, 'json': 's7', 'xml': 's7'},
            's2': {'this': s2, 'json': 's6', 'xml': 's6'},
            's3': {'this': s3, 'json': 's10', 'xml': 's10'},
            's4': {'this': s4, 'json': 's2', 'xml': 's2'},
            's5': {'this': s5, 'json': 's3', 'xml': 's7'},
            's6': {'this': s6, 'json': 's8', 'xml': 's9'},
            's7': {'this': s7, 'json': 's6', 'xml': 's6'},
            's8': {'this': s8, 'json': 's8', 'xml': 's8'},
            's9': {'this': s9, 'json': 's9', 'xml': 's9'},
            's10': {'this': s10, 'json': 's1', 'xml': 's4'},
        }
    '''
    map_dict = {}
    try:
        with open(file_name,'r')as f:
            content = ''
            while True:
                read_content = f.read(1024)
                if read_content:
                    content += read_content
                else:
                    break
        text_dict = eval(content)
        if type(text_dict == dict):
            for key, value in text_dict.items():
                map_dict['s' + str(key)] = {}
                map_dict['s' + str(key)]['this'] = 's' + str(key)
                map_dict['s' + str(key)]['json'] = 's' + str(value[0])
                if len(value) == 1:
                    map_dict['s' + str(key)]['xml'] = 's' + str(value[0])
                else:
                    map_dict['s' + str(key)]['xml'] = 's' + str(value[1])
    except Exception as e:
        print(e)
    else:
        return map_dict


@app.route('/index', methods=["GET", "POST"])
def conversation_handler():
    username = request.args['username']
    nextfunc = request.args.get('nextfunc')  # user select
    next = request.cookies.get("next", '')  # browser saved
    invoke_map = get_map('./coordination_protocol.txt')
    if next == '':
        response = eval(invoke_map.get(nextfunc)['this'])(username, map_dict=invoke_map.get(nextfunc))
    elif next == 's0':
        response = make_response(jsonify({'errno': 1001, 'errmsg': "invoke finish"}))
        response.delete_cookie('next')
    else:
        response = eval(invoke_map.get(next)['this'])(username, map_dict=invoke_map[next])
    return response




if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
