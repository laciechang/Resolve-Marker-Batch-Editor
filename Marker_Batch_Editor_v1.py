# -*- coding:utf-8 -*-
# Author: 张来吃
# Version: 1.0.0
# Contact: laciechang@163.com

# -----------------------------------------------------
# This script must be run in DaVinci Resolve only.
# -----------------------------------------------------


import re, math

regex = False

marker_color = ['Blue','Cyan','Green','Yellow','Red','Pink','Purple','Fuchsia','Rose','Lavender','Sky','Mint','Lemon','Sand','Cocoa','Cream']

def _exit(ev):
    disp.ExitLoop()

def getresolve(app='Resolve'):
    dr = bmd.scriptapp(app)
    return dr

def this_pj():
    pj_manager = getresolve().GetProjectManager()
    current_pj = pj_manager.GetCurrentProject()
    return current_pj

def this_timeline():
    return this_pj().GetCurrentTimeline()

def frame_to_index(i):
    lenth = len(str(max(read_all_marker().keys())))
    b = int(math.pow(10, int(lenth)))
    o = str(b+int(i))[1:]
    return o

def read_all_marker():
    mks = this_timeline().GetMarkers()
    return mks

def add_markers(frameId, color, name, note, duration, customData=''):
    o = this_timeline().AddMarker(frameId, color, name, note, duration, customData)
    return o

def del_markers(by, frameNum, color):
    if by is 'frame':
        o = this_timeline().DeleteMarkerAtFrame(frameNum)
    elif by is 'color':
        o = this_timeline().DeleteMarkersByColor(color)
    else:
        o = False
    return o

def replace_marker(type, mk_frameId, color, name, note, duration, customData):
    del_markers(type, mk_frameId, color)
    add_markers(mk_frameId, color, name, note, duration, customData)

def edit_marker(type, before, after):
    pattern = re.compile(str(before))
    all_marker = read_all_marker()
    for mk_frameId in all_marker:
        mk = all_marker[mk_frameId]
        color = str(mk['color'])
        duration = int(mk['duration'])
        note = str(mk['note'])
        name = str(mk['name'])
        customData = mk['customData']
        if type is 'color':
            if before==color:
                del_markers('frame', mk_frameId, color)
                add_markers(mk_frameId, after, name, note, duration, customData)
            else:
                pass
        elif type is 'name':
            if regex is True:
                if re.search(pattern, name) is not None:
                    new_name = re.sub(pattern, after, name)
                    replace_marker('frame', mk_frameId, color, new_name, note, duration, customData)
                else:
                    pass
            else:
                new_name = name.replace(before, after)
                replace_marker('frame', mk_frameId, color, new_name, note, duration, customData)
        elif type is 'note':
            if regex is True:
                if re.search(pattern, name) is not None:
                    new_note = re.sub(pattern, after, note)
                    replace_marker('frame', mk_frameId, color, name, new_note, duration, customData)
                else:
                    pass
            else:
                new_note = note.replace(before, after)
                replace_marker('frame', mk_frameId, color, name, new_note, duration, customData)
        else:
            pass
        print(color, duration, note, name, customData)

def _edit_color(ev):
    before = itm['color_a'].CurrentText
    after = itm['color_b'].CurrentText
    if before==after:
        pass
    else:
        itm['edit_color'].Enabled = False
        itm['edit_color'].Text = '喝口茶'
        edit_marker('color', before, after)
        itm['edit_color'].Enabled = True
        itm['edit_color'].Text = '替换'
    

def _edit_notes(ev):
    global regex
    before = itm['notes_a'].Text
    after = itm['notes_b'].Text
    if before==after:
        regex = bool(1-regex)
        pass
    else:
        itm['edit_notes'].Enabled = False
        itm['edit_notes'].Text = '喝口茶'
        edit_marker('note', before, after)
        itm['edit_notes'].Enabled = True
        itm['edit_notes'].Text = '修改'
    if regex is True:
        itm['notes_a'].PlaceholderText = '正则'
        itm['name_a'].PlaceholderText = '正则'
    else:
        itm['name_a'].PlaceholderText = ''
        itm['notes_a'].PlaceholderText = ''

def _edit_name(ev):
    global regex
    before = itm['name_a'].Text
    after = itm['name_b'].Text
    if before==after:
        regex = bool(1-regex)
        pass
    else:
        itm['edit_name'].Enabled = False
        itm['edit_name'].Text = '喝口茶'
        edit_marker('name', before, after)
        itm['edit_name'].Enabled = True
        itm['edit_name'].Text = '修改'
    if regex is True:
        itm['notes_a'].PlaceholderText = '正则'
        itm['name_a'].PlaceholderText = '正则'
    else:
        itm['name_a'].PlaceholderText = ''
        itm['notes_a'].PlaceholderText = ''

def _del_by_color(ev):
    targ = itm['color_a'].CurrentText
    del_markers('color', '', targ)

def main_ui(ui):
    window = ui.VGroup({"Spacing": 10,},[
        ui.HGroup({"Spacing": 10, "Weight": 0,},[ 
            ui.Label({ "ID": "color","Text": "Color"}),
            ui.ComboBox({ "ID": "color_a","Weight": 4}),
            ui.ComboBox({ "ID": "color_b","Weight": 4}),
            ui.Button({ "ID": "edit_color", "Text": "替换","Weight": 0}),
        ]),
        ui.HGroup({"Spacing": 10, "Weight": 0,},[
            ui.HGap(),
            ui.Button({ "ID": "del_by_color", "Text": "删除","Weight": 0}),
        ]),
        ui.HGroup({"Spacing": 10, "Weight": 0,},[ 
            ui.Label({ "ID": "notes","Text": "Notes"}),
            ui.LineEdit({ "ID": "notes_a","Weight": 4}),
            ui.LineEdit({ "ID": "notes_b","Weight": 4}),
            ui.Button({ "ID": "edit_notes", "Text": "修改","Weight": 0}),
        ]),
        ui.HGroup({"Spacing": 10, "Weight": 0,},[ 
            ui.Label({ "ID": "name","Text": "Name"}),
            ui.LineEdit({ "ID": "name_a","Weight": 4}),
            ui.LineEdit({ "ID": "name_b","Weight": 4}),
            ui.Button({ "ID": "edit_name", "Text": "修改","Weight": 0}),
        ]),
        ])
    return window


if __name__ == '__main__':
    fu = bmd.scriptapp('Fusion')

    ui = fu.UIManager
    disp = bmd.UIDispatcher(ui)

    window_01 = main_ui(ui)

    dlg = disp.AddWindow({ 
                        "WindowTitle": "Marker Editor", 
                        "ID": "MyWin", 
                        "Geometry": [ 
                                    600, 600, 
                                    600, 160
                         ], 
                        },
    window_01)

    itm = dlg.GetItems()

    itm['color_a'].AddItems(marker_color)
    itm['color_b'].AddItems(marker_color)

    dlg.On.edit_color.Clicked = _edit_color
    dlg.On.edit_name.Clicked = _edit_name
    dlg.On.edit_notes.Clicked = _edit_notes
    dlg.On.del_by_color.Clicked = _del_by_color
    

    dlg.On.MyWin.Close = _exit
    dlg.Show()
    disp.RunLoop()
    dlg.Hide()