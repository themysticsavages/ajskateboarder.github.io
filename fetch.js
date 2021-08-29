window.onload = function() {
    fetch('https://api.github.com/search/repositories?q=user:themysticsavages&sort=updated&order=desc')
        .then((response) => response.json())
        .then((project) => {
            var projs = [project['items'][0], project['items'][1], project['items'][2]]
            document.getElementById('proj1').innerHTML = `&nbsp;${projs[0]['name']}<br><sub>&nbsp;${projs[0]['description']}</sub>`
            document.getElementById('proj2').innerHTML = `&nbsp;${projs[1]['name']}<br><sub>&nbsp;${projs[1]['description']}</sub>`
            document.getElementById('proj3').innerHTML = `&nbsp;${projs[2]['name']}<br><sub>&nbsp;${projs[2]['description']}</sub>`

            document.getElementById('id1').href = projs[0]['html_url']
            document.getElementById('id2').href = projs[1]['html_url']
            document.getElementById('id3').href = projs[2]['html_url']
    })
}