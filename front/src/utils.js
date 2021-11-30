var capitalize = (text) => {
    // Capitalize the first letter of
    // a word

    var tokens = [text]

    for (var i = 0; i < tokens.length; i++) {
        tokens[i] = tokens[i].charAt(0).toUpperCase() + tokens[i].slice(1)
    }

    //Join all the elements of the array back into a string 
    //using a blankspace as a separator 
    const result = tokens.join(' ');
    return result
}


export {
    capitalize
}
