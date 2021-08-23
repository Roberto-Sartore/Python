m = float(input('Digite uma distacia em metros '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('A medida de {}m Corresponde a {:.0f}dm, {:.0f}cm e {:.0f}mm '.format(m,dm,cm,mm))
print('A medida de {}m Corresponde a {:.2f}dam, {:.2f}hm e {:.3f}km '.format(m,dam,hm,km))
