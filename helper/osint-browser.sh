#!/bin/sh

search_term="$1"
template_query="_,temp,_"
delimiter="_,del,_"
browser_command="firefox --new-tab"

querys="https://www.google.com/search?q=${template_query}${delimiter}${search_term} site:cvedetails.com inurl:/cve/
https://github.com/swisskyrepo/PayloadsAllTheThings/search?q=${template_query}${delimiter}${search_term}
https://www.google.com/search?q=${template_query}${delimiter}${search_term} inurl:walkthrough site:hackingarticles.in
https://twitter.com/search?q=${template_query}&src=typed_query${delimiter}${search_term}
https://www.google.com/search?q=${template_query}${delimiter}${search_term} inurl:reports site:hackerone.com
https://github.com/search?q=${template_query}${delimiter}${search_term}
https://www.google.com/search?q=${template_query}${delimiter}${search_term} site:resources.infosecinstitute.com inurl:walkthrough
https://www.google.com/search?q=${template_query}${delimiter}${search_term} site:medium.com inurl:(walkthrough|ctf|vulnhub) -'host a CTF' -'Hosting CTF' -'Organize a CTF'
https://www.google.com/search?q=${template_query}${delimiter}${search_term} site:medium.com inurl:CVE
https://www.google.com/search?q=${template_query}${delimiter}${search_term} site:blog.csdn.net inurl:details intext:(ctf|oscp|virtualhackinglabs)
https://www.google.com/search?q=${template_query}${delimiter}${search_term} site:0xdf.gitlab.io -inurl:tags inurl:html
https://www.google.com/search?q=${template_query}${delimiter}${search_term} inurl:ctf site:bootlesshacker.com
https://www.google.com/search?q=${template_query}${delimiter}${search_term} site:fdlucifer.github.io -inurl:(page and archives and categories) intext:(vulnhub|Hack-The-Box)
https://www.google.com/search?q=${template_query}${delimiter}${search_term} site:book.hacktricks.xyz"

echo "$querys" | while read -r q; do
  url="$(echo "$q" | awk -F "$delimiter" '{print $1}')"
  query_param="$(echo "$q" | awk -F "$delimiter" '{print $2}')"
  encoded_query_param="$(echo "$query_param" | python3 -c "import sys, urllib.parse as ul; print(ul.quote_plus(sys.stdin.read()[:-1]))")"
  full_url="$(echo "$url" | awk -v t="$template_query" -v e="$encoded_query_param" '{gsub(t,e); print}')"
  echo "Opening: $full_url"
  $browser_command "$full_url"
  sleep 1.5 # prevent google timeout
done
$browser_command 'https://ippsec.rocks/'
