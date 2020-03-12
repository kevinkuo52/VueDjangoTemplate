import CoreAPI from './CoreAPI'

export default {
    searchPaper () {
        return CoreAPI().get('/paper')
    }
}