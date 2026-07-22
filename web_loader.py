from langchain_community.document_loaders import WebBaseLoader

url='https://www.amazon.in/Portronics-Wireless-Optical-Orientation-Adjustable/dp/B0B296NTFV/ref=sr_1_16?adgrpid=1322714098021561&dib=eyJ2IjoiMSJ9.iOn2ZuvIqdj3mbBqR5ZlAPF-G2inQZQhpNCTTwzhIB86QuLL3q4n1ojMCydWEnokq8yjdQqbk9cpGzL_BkAMETF0nNABek8awUQIP_NEzt8NqHaUTM-Zw_tW2qQ5JVt2KyQ1rs1h01-91J4nMUSSVBU3ftm97IYjf915oJi3c2ubInLHWkuxC9g9uanoxsQ2WwW3TB1BGjXZpoGArfVOFbeNT9BTRUyfWwIZD8JJRWifAoqRjo5Q_XMwkVqbesOXvkcjM_vP12PYeeMIWC60878FQcsKPXX8aCssv-eOCs8.TiGvZGYXBSWdTOewA0IBqE4__cSJDWevizJIBWGCcd4&dib_tag=se&hvadid=82669890077100&hvbmt=be&hvdev=c&hvlocphy=149903&hvnetw=o&hvqmt=e&hvtargid=kwd-82670515805048%3Aloc-90&hydadcr=26727_2475684&keywords=flipkart+online+shopping&mcid=1350bbd75b8a3786bea44c79f0a75293&qid=1779010724&sr=8-16'
loader=WebBaseLoader(url)

docs=loader.load()

text=docs[0].page_content

print(text)
