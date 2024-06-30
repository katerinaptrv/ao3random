document.getElementById("goButton").addEventListener("click", async () => {
            const searchUrl = document.getElementById("searchUrl").value;

            if (!searchUrl) {
                alert("Please enter a valid AO3 search or bookmarks URL.");
                return;
            }
			
			 const loading = document.getElementById("loading");
			 loading.style.display = "block";

            const response =  await fetch( window.location.href+'fetch', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/x-www-form-urlencoded'
					},
					body: `url=${encodeURIComponent(searchUrl)}`
    });
            const html = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, "text/html");

			let fanficLinks = doc.querySelectorAll('h4.heading > a[href*="works"]');
			let randomIndex = Math.floor(Math.random() * fanficLinks.length);
			let randomFanficLink = fanficLinks[randomIndex].href;

			if (randomFanficLink) {
				 console.log(randomFanficLink);
				 randomFanficLink = randomFanficLink.replace(window.location.href, '')
				 document.getElementById("loading").style.display = 'none';
				 window.open('https://archiveofourown.org/'+randomFanficLink, '_blank');
			} else {
				alert('No fanfics found on the search result page.');
			}
        });