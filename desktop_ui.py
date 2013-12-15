import wx
import sys
import os
from util.kkfile import open_file
from model import BookFile


class BookListFrame(wx.Frame):
    def __init__(self, bookinfo):
        self.bookinfo = bookinfo
        wx.Frame.__init__(self, None, -1, 'lean book')
        self.list = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.list.InsertColumn(1001, 'book list', format=wx.LIST_FORMAT_LEFT, width=500) 

        self.idx2name = {}
        for book in bookinfo.get_booklist():
            for bookname in bookinfo.get_origname(book):
                self.idx2name[self.list.InsertStringItem(sys.maxint, bookname)] = book

        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnOpenFile, self.list)  # dlick to open a file

    def OnOpenFile(self, event):
        open_file(self.bookinfo.get_filepath(self.idx2name[event.GetIndex()]))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frm = BookListFrame(BookFile('a'))
    frm.Show()
    app.MainLoop()
