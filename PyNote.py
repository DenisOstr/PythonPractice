import wx
import os

class Window(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title = title, size = (640, 480))

		self.Modify = False
		self.LastSave = ""
		self.replace = False
		
		self.SetIcon(wx.Icon('note.ico', wx.BITMAP_TYPE_ICO))
		self.TextField = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
		self.TextField.SetFocus()
		self.Show(True)
		
		#--------------------------------------------------------------------------------------------#
		
		File = wx.Menu()
		
		newItem = wx.MenuItem(File, wx.ID_NEW, "New", "Push the button to create new file")
		File.Append(newItem)
		
		File.AppendSeparator()
		
		openItem = wx.MenuItem(File, wx.ID_OPEN, "Open", "Push the button to open file")
		File.Append(openItem)
		
		saveItem = wx.MenuItem(File, wx.ID_SAVE, "Save", "Push the button to save file")
		File.Append(saveItem)
		
		saveAsItem = wx.MenuItem(File, wx.ID_SAVEAS, "Save As", "Push the button to save file as")
		File.Append(saveAsItem)
		
		File.AppendSeparator()
		
		exitItem = wx.MenuItem(File, wx.ID_EXIT, "Exit", "Push the button to leave this application")
		File.Append(exitItem)
		
		#--------------------------------------------------------------------------------------------#
		
		Edit = wx.Menu()
		
		undoItem = wx.MenuItem(Edit, wx.ID_UNDO, "Undo", "Push the button to return back on text")
		Edit.Append(undoItem)
		
		Edit.AppendSeparator()
		
		cutItem = wx.MenuItem(Edit, wx.ID_CUT, "Cut", "Puch the button to cut text")
		Edit.Append(cutItem)
		
		copyItem = wx.MenuItem(Edit, wx.ID_COPY, "Copy", "Puch the button to copy text")
		Edit.Append(copyItem)
		
		pasteItem = wx.MenuItem(Edit, wx.ID_PASTE, "Paste", "Puch the button to paste text")
		Edit.Append(pasteItem)
		
		deleteItem = wx.MenuItem(Edit, wx.ID_DELETE, "Delete", "Puch the button to delete text")
		Edit.Append(deleteItem)
		
		Edit.AppendSeparator()
		
		selectAllItem = wx.MenuItem(Edit, wx.ID_SELECTALL, "Select All", "Push the button to select all the text")
		Edit.Append(selectAllItem)
		
		#--------------------------------------------------------------------------------------------#
		
		Format = wx.Menu()
		
		chooseColorItem = wx.MenuItem(Format, wx.ID_ANY, "Choose Color", "Push the button to choose color")
		Format.Append(chooseColorItem)
		
		Format.AppendSeparator()
		
		chooseFontItem = wx.MenuItem(Format, wx.ID_ANY, "Choose Font", "Push the button to choose font")
		Format.Append(chooseFontItem)
		
		#--------------------------------------------------------------------------------------------#
		
		View = wx.Menu()
		
		statusBarItem = wx.MenuItem(View, wx.ID_ANY, "Status Bat", "Show Status Bar")
		View.Append(statusBarItem)
		
		#--------------------------------------------------------------------------------------------#
		
		Help = wx.Menu()
		
		aboutItem = wx.MenuItem(Help, wx.ID_ABOUT, "About", "Push the button to get an information about this application")
		Help.Append(aboutItem)
		
		#--------------------------------------------------------------------------------------------#
		
		MenuBar = wx.MenuBar()
		
		MenuBar.Append(File, 'File')
		MenuBar.Append(Edit, 'Edit')
		MenuBar.Append(Format, 'Format')
		MenuBar.Append(View, 'View')
		MenuBar.Append(Help, 'Help')
		self.SetMenuBar(MenuBar)
		
		#--------------------------------------------------------------------------------------------#
		
		self.Bind(wx.EVT_MENU, self.OnNew, newItem)
		self.Bind(wx.EVT_MENU, self.OnOpen, openItem)
		self.Bind(wx.EVT_MENU, self.OnSave, saveItem)
		self.Bind(wx.EVT_MENU, self.OnSaveAs, saveAsItem)
		self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
		
		self.Bind(wx.EVT_MENU, self.OnUndo, undoItem)
		self.Bind(wx.EVT_MENU, self.OnCut, cutItem)
		self.Bind(wx.EVT_MENU, self.OnCopy, copyItem)
		self.Bind(wx.EVT_MENU, self.OnPaste, pasteItem)
		self.Bind(wx.EVT_MENU, self.OnDelete, deleteItem)
		self.Bind(wx.EVT_MENU, self.OnSelectAll, selectAllItem)
		
		self.Bind(wx.EVT_MENU, self.OnChooseColor, chooseColorItem)
		self.Bind(wx.EVT_MENU, self.OnChooseFont, chooseFontItem)
		
		self.Bind(wx.EVT_MENU, self.OnStatusBar, statusBarItem)
		
		self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
		
		self.TextField.Bind(wx.EVT_TEXT, self.OnTextChanged)
		self.TextField.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
		
		self.Bind(wx.EVT_CLOSE, self.OnExit)
		
		self.StatusBar()
	

	#--------------------------------------------------------------------------------------------#
	
	
	def OnNew(self, event):
		if self.Modify:
			QuestionDialog = wx.MessageDialog(self, 'Save before create new file?', '', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION)
			Answer = QuestionDialog.ShowModal()
			
			if Answer == wx.ID_YES:
				self.OnSave(event)
				self.TextField.SetValue("")
				
				if not self.Modify:
					self.TextField.SetValue("")
			else:
				self.TextField.SetValue("")
		else:
			self.TextField.SetValue("")
			
		window.SetTitle("Untitled" + " - PyNote")
		
		
	def OnOpen(self, event):
		FName = os.path.basename(self.LastSave)
		
		if self.Modify:
			QuestionDialog = wx.MessageDialog(self, "Save changes?", "", wx.YES_NO | wx.YES_DEFAULT | wx.CANCEL | wx.ICON_QUESTION)
			Answer = QuestionDialog.ShowModal()
			
			if Answer == wx.ID_YES:
				self.OnSave(event)
				self.DoOpen()
			elif Answer == wx.ID_CANCEL:
				QuestionDialog.Destroy()
			else:
				self.DoOpen()
		else:
			self.DoOpen()
		
	
	def DoOpen(self):
		self.dirname = " "
		openDialog = wx.FileDialog(self, "Choose a file to open", self.dirname, " ", "*.*", wx.FD_OPEN)
		
		if openDialog.ShowModal() == wx.ID_OK:
			#path = openDialog.GetPath()
			
			try:
				'''file = open(path, 'r')
				text = file.read()
				file.close()
				
				self.TextField.WriteText(text)
				self.LastSave = path
				self.Modify = False'''
				
				self.filename = openDialog.GetFilename()
				self.dirname = openDialog.GetDirectory()
				file = open(os.path.join(self.dirname, self.filename), "r")
			
				self.TextField.SetValue(file.read())
				file.close()
				window.SetTitle(self.filename + " - PyNote")
				
			except IOError:
				ErrorDialog = wx.MessageDialog(self, "Error opening file\n" + str(IOError))
				ErrorDialog.ShowModal()
				
			except UnicodeDecodeError:
				ErrorDialog = wx.MessageDialog(self, "Error Opening file\n" + str(UnicodeDecodeError))
				ErrorDialog.ShowModal()
				
		openDialog.Destroy()
		
		
	def OnSave(self, event):
		if self.LastSave:
			try:
				file = open(self.LastSave, 'w')
				text = self.TextField.GetValue()
				file.write(text)
				file.close()
				self.Modify = False
				
			except IOError:
				ErrorDialog = wx.MessageDialog(self, "Error saving file\n" + str(IOError))
				ErrorDialog.ShowModal()
		else:
			self.OnSaveAs(event)
		
		
	def OnSaveAs(self, event):
		saveDialog = wx.FileDialog(self, "Save file as...", " ", " ", "*.*", wx.FD_SAVE)
		
		if saveDialog.ShowModal() == wx.ID_OK:
			#path = saveDialog.GetPath()
			
			try:
				'''file = open(path, 'w')
				text = self.TextField.GetValue()
				file.write(text)
				file.close()
				self.LastSave = os.path.basename(path)
				self.Modify = False'''
				
				text = self.TextField.GetValue()
			
				self.filename = saveDialog.GetFilename()
				self.dirname = saveDialog.GetDirectory()
				file = open(os.path.join(self.dirname, self.filename), 'w')
				file.write(text)
				file.close()
				self.LastSave = os.path.basename(os.path.join(self.dirname, self.filename))
				self.Modify = False
				window.SetTitle(self.filename + " - PyNote")
			
			except:
				ErrorDialog = wx.MessageDialog(self, "Error saving file\n" + str(IOError))
				ErrorDialog.ShowModal()
				
		saveDialog.Destroy()
	

	def OnTextChanged(self, event):
		self.Modify = True
		event.Skip()
	
		
	def OnExit(self, event):
		if self.Modify:
			QuestionDialog = wx.MessageDialog(self, 'Save before Exit?', '', wx.YES_NO | wx.YES_DEFAULT | wx.CANCEL | wx.ICON_QUESTION)
			Answer = QuestionDialog.ShowModal()
			
			if Answer == wx.ID_YES:
				self.OnSave(event)
				
				if not self.Modify:
					wx.Exit()
			elif Answer == wx.ID_CANCEL:
				QuestionDialog.Destroy()
			else:
				self.Destroy()
		else:
			self.Destroy()
	

	#--------------------------------------------------------------------------------------------#
	
	
	def OnUndo(self, event):
		pass
		
		
	def OnCut(self, event):
		self.TextField.Cut()
		
		
	def OnCopy(self, event):
		self.TextField.Copy()
		
		
	def OnPaste(self, event):
		self.TextField.Paste()
		
		
	def OnDelete(self, event):
		textRemove, to = self.TextField.GetSelection()
		self.TextField.Remove(textRemove, to)
		
		
	def OnSelectAll(self, event):
		self.TextField.SelectAll()
		
		
	#--------------------------------------------------------------------------------------------#
	
	
	def OnChooseColor(self, event):
		pass
		
	
	def OnChooseFont(self, event):
		pass
		
		
	#--------------------------------------------------------------------------------------------#
	

	def OnStatusBar(self, event):
		if self.statusbar.IsShown():
			self.statusbar.Hide()
		else:
			self.statusbar.Show()
			
	
	def StatusBar(self):
		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetFieldsCount(3)
		self.statusbar.SetStatusWidths([-5, -2, -1])
		
		
	#--------------------------------------------------------------------------------------------#	
		
		
	def OnAbout(self, event):
		aboutDialog = wx.MessageDialog(self, "PyNote\t\n Version:\t\t 1.19.08 \nDenis Ostrovsky 2017", "About PyNote", wx.OK)
		aboutDialog.ShowModal()
	
	
	#--------------------------------------------------------------------------------------------#
	
	
	def OnKeyDown(self, event):
		keyCode = event.GetKeyCode()
		
		if keyCode == wx.WXK_INSERT:
			if not self.replace:
				self.replace = True
			else:
				self.replace = False
				
		event.Skip()
	

app = wx.App()
window = Window(None, "Untitled" + " - PyNote")
app.MainLoop()