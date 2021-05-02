import PySimpleGUI as sg      

layout = [      
			[sg.Text('Please enter your Name, Address, Phone')],      
			[sg.Text('Name', size=(15, 1)), sg.InputText('1', key='_name_')],      
			[sg.Text('Address', size=(15, 1)), sg.InputText('2', key='_address_')],      
			[sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='_phone_')],      
			[sg.Submit(), sg.Cancel()]      
			]      

window = sg.Window('Simple data entry window', layout)  
event, values = window.Read()    

sg.Popup(event, values, values['_name_'], values['_address_'], values['_phone_'])      