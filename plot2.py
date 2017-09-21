import matplotlib.pyplot as plt

f, ax = plt.subplots(2, 6, sharey='row')

title = [
    'Profundidad (m)',
    'Tipo de Perforación',
    'Fecha',
    'Revestimiento',
    'Prof.Agua (m)',
    'Notas']

for subp, titl in zip(ax[0], title):
    subp.tick_params(labelbottom='off',labelleft='off', left='off')
    subp.text(0.5, 0.05, titl, color='k', ha='center', va='bottom', size='x-small', rotation=90)

for subp, titl in zip(ax[1], title):
    subp.tick_params(labelbottom='off', direction='in', pad=-15)
    #subp.set_title(titl)
    subp.text(0.5, 0.8, titl, color='k', ha='center', rotation=90)
    #subp.title.set_rotation(90)

plt.ylim(ymin=10, ymax=0)

ax[1,1].axhline(y=1)
ax[1,1].axhline(y=3)
ax[1,1].axhline(y=5)


ax[1,3].axhline(y=6)
ax[1,3].axhline(y=7)
ax[1,3].axhline(y=8)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0, hspace=0)

plt.show()
