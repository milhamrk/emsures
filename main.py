import trendln
import matplotlib.pyplot as plt
import yfinance as yf
tick = yf.Ticker('^JKSE')
hist = tick.history(period="max", rounding=True)
mins, maxs = trendln.calc_support_resistance(hist[-1000:].Close, accuracy=8)
minimaIdxs, pmin, mintrend, minwindows = trendln.calc_support_resistance((hist[-1000:].Low, None), accuracy=8)
mins, maxs = trendln.calc_support_resistance((hist[-1000:].Low, hist[-1000:].High), accuracy=8)
(minimaIdxs, pmin, mintrend, minwindows), (maximaIdxs, pmax, maxtrend, maxwindows) = mins, maxs
minimaIdxs, maximaIdxs = trendln.get_extrema(hist[-1000:].Close, accuracy=8)
maximaIdxs = trendln.get_extrema((None, hist[-1000:].High), accuracy=8)
minimaIdxs, maximaIdxs = trendln.get_extrema((hist[-1000:].Low, hist[-1000:].High), accuracy=8)
fig = trendln.plot_support_resistance(hist[-1000:].Close, accuracy=8)
plt.savefig('suppres.svg', format='svg')
plt.show()
plt.clf()
fig = trendln.plot_sup_res_date((hist[-1000:].Low, hist[-1000:].High), hist[-1000:].index, accuracy=8)
plt.savefig('suppres.svg', format='svg')
plt.show()
plt.clf()
curdir = '.'
trendln.plot_sup_res_learn(curdir, hist)