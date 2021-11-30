import { capitalize } from '../utils'

export default {
    filters: {
        title(value) {
            return capitalize(value)
        }
    }
}
