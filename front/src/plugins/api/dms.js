export default ($axios) => ({
    get(userId) {
        return $axios({
            method: 'get',
            url: `/direct-messages/${userId}`,
            data: { user_id: userId }
        })
    }
})
