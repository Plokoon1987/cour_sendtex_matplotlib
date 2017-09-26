import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from matplotlib.backends.backend_pdf import PdfPages

from matplotlib.ticker import FormatStrFormatter

PageSizeMm = {
    'A4':(210,297), 'A4_L':(297,210),
    'A3':(297,420),'A3_L':(420,297)
    }
    
PageSizeInch = {
    'A4':(8.3,11.7), 'A4_L':(11.7,8.3),
    'A3':(11.69,16.4),'A3_L':(16.4,11.69)
    }

fig = plt.figure(figsize=PageSizeInch['A3_L'])

print(fig.get_figwidth())
print(fig.get_figheight())


# ***** Outside Box *****
# ********************
Out_box = gridspec.GridSpec(1, 1)
#Out_box.update(left=0.0572656, right=0.9761393333, bottom=0.0504744872, top=0.9327006838)
Out_box.update(left=0.0572656, right=0.9761393333, bottom=0.0504744872, top=1)
O_box = plt.subplot(Out_box[0])
O_box.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')


'''


min_depth = 0
max_depth = 10

gs = gridspec.GridSpec(6, 42)

# ***** CABECERA *****
# ********************

# **** Tamaño ****

cabecera = plt.subplot(gs[0, :-1])
cabecera.set_xlim(xmin=0, xmax=38.5)

# Tamaños Standard:
#   -A3 = (xmin=0, xmax=38.5)

# **** Lineas de Separación ****
cabc_spacing = [7,16,22.2,28.8,32.5,38.5]
for spac in cabc_spacing:
    cabecera.axvline(x=spac, linewidth=0.5, color='k')




plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0, hspace=0)
'''
#plt.show() ### ADJUSTS PDF too




fig.savefig(filename='/home/froylan/windows/VBox/multipage1.pdf',
    edgecolor='k',
    orientation='landscape',
    papertype='A3',
    format='pdf',
    )
