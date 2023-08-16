import { App, ComponentCustomProperties, Ref } from 'vue'

declare type DictionnaryKey = {
    key: string
}

/** Creates a VueLocalStorage instance that can be used by a Vue app */
export declare function createLocalStorage(options?: BaseOptions): VueLocalStorage

/** Creates a VueSession instance that can be used by a Vue app */
export declare function createVueSession(options?: VueSessionOptions): VueSession

export declare interface BaseOptions {
    /** The default session key (default: vue-session) */
    sessionKey?: number
    /** Initial values with which to initialize the storage */
    initial?: object
}

/** 
 * VueLocalStorage allows serializing and deserializing
 * data in the base Window locale storage
 */
export declare interface VueLocalStorage {
    /** The default session key (defaults: vue-session) */
    readonly DEFAULT_KEY_NAME: string
    /**
     * Returns all items saved in the localStorage
     *
     * @returns dictionnary
     */
    readonly data: object

    constructor(options?: BaseOptions): void
    /**
     * Returns the value store under a given key
     *
     * @param key - key to use
     * @returns an object, a number or an array
     */
    retrieve (key: DictionnaryKey): object | string | number
    /**
     * Creates a new record under the given key
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns null
     */
    create(key: DictionnaryKey, value: unknown): void
    /**
     * Creates a new record under the given key but transforms
     * the incoming value to a base 64 string
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns null
     */
    b64Create (key, value): void
    /**
     * Returns the transformed b64 value stored under a given key
     *
     * @param key - key to use
     * @returns an object, a number or an array
     */
    b64Retrieve (key): string
    /**
     * Gets the b64 value, transforms it and 
     * then immediately deletes it
     * 
     * @param key - key under which to save the element
     * @returns any
     */
    b64GetDelete (key): string
    /**
     * Checks if a value exists in a dictionnary
     * 
     * @param key - key under which to save the element
     * @returns boolean
     */ 
    exists(key: DictionnaryKey): boolean
    /**
     * Gets a value and immediately deletes it
     * 
     * @param key - key under which to save the element
     * @returns any
     */
    getDelete(key: DictionnaryKey): any
    /**
     * Increment a value by one
     * 
     * @param key - key under which to increment the element
     * @returns null
     */
    increment (key: DictionnaryKey): void
    /**
     * Decrement a value by one
     * 
     *  @param key - key under which to decrement the element
     *  @returns null
     */
    decrement (key: DictionnaryKey): void
    /**
     * Removes an element stored under a given key
     *
     * @param key key of the element to remove
     * @returns null
     */
    remove(key: DictionnaryKey): void
    /**
     * Increment a value by a certain quantity
     * 
     * @param key - key under which to increment the element
     * @param k - value to increment by
     * @returns null
     */
    incrementBy (key: DictionnaryKey, k: number = 1): void
    /**
     * Decrement a value by a certain quantity
     * 
     * @param key - key under which to increment the element
     * @param k - value to decrement by
     * @returns null
     */
    decrementBy (key: DictionnaryKey, k: number = 1): void
    /**
     * Increment the value located under a dictionnary
     * key by a certain quantity
     * 
     * @param key - key containing the dictionnary to update
     * @param keyToUpdate - key under the dictionnary to increment
     * @param k - value to increment by
     * @returns null
     */
    incrementDictKeyBy (key: string, keyToUpdate: string, k: number = 1): void
    /**
     * Decrement the value located under a dictionnary
     * key by a certain quantity
     * 
     * @param key - key containing the dictionnary to update
     * @param keyToUpdate - key under the dictionnary to Decrement
     * @param k - value to decrement by
     * @returns null
     */
    decrementDictKeyBy (key: string, keyToUpdate: string, k: number = 1): void
    /**
     * Gets or creates a new value if it does not exist
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns any
     */
    getOrCreate (key: DictionnaryKey, value: any): any
    /**
     * Pushes a value in a list
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns null
     */
    listPush (key: DictionnaryKey, value: any): void
    /**
     * Pushes a value in a list only if it does not alreay exist
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns null
     */
    listPushUnique (key: DictionnaryKey, value: any): void
    /**
     * Like listPush but will create a new list if it
     * does not exist
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns null
     */
    defaultList (key: DictionnaryKey, value: any): void
    /**
     * Merges two lists under a given key
     *
     * @param key - key under which to merge the elements
     * @param values - array to merge
     * @returns null
     */
    listMerge (key: DictionnaryKey, values: object): void
    /**
     * Counts the number of items under a given list
     *
     * @param key - key under which to merge the elements
     * @returns number
     */
    listCount (key: DictionnaryKey): number
    /**
     * Toggles a value under a given key
     *
     * @param key - key under which to save the element
     * @returns null
     */
    toggle(key: DictionnaryKey): void
    
    install(app: App): void
}

/** Possible options for VueSession */
export declare interface VueSessionOptions extends BaseOptions {
    /** Persist the data in the local storage */
    persistent?: boolean
}

/** 
 * VueSession allows serializing and deserializing
 * data easily in the base Window session storage
 */
export declare interface VueSession {
    /** The default session key (defaults: vue-session) */
    readonly DEFAULT_KEY_NAME: string
    /**
     * Returns all items saved in the storage
     *
     * @returns dictionnary
     */
    readonly data: object

    constructor(options?: VueSessionOptions): void
    /**
     * Creates a new record under the given global key
     *
     * @param key - key under which to save the element
     * @param value - number, array or dictionnary
     * @returns null
     */
    create(key: DictionnaryKey, value: unknown): void
    /**
     * Returns the value store under a given key
     *
     * @param key - key to use
     * @returns an object, a number or an array
     */
    retrieve(key: DictionnaryKey): number | string | number[] | string[]
    /**
     * Removes an element stored under a given key
     *
     * @param key key of the element to remove
     * @returns null
     */
    remove(key: DictionnaryKey): void
    /**
     * Renews the session key
     */
    renew(): void
    /**
     * Clears all data stored under the global key
     */
    clear(): void
    /**
     * Checks whether a key exists in the storage
     *
     * @param key key of the element to remove
     * @returns Boolean
     */
    contains(key: DictionnaryKey): boolean
    /**
     * Destroys the session
     */
    destroy(): void
    /**
     * Tries to get a key and eventually creates
     * a new record with the given value if it
     * does not exist
     *
     * @param key - key of the element to remove
     * @param defaultValue - key of the element to remove
     */
    getOrCreate(key: DictionnaryKey, defaultValue: unknown): number | object
    /**
     * Toggle a boolean stored under a given key
     * 
     * @param key - key of the element to toggle
     */
    toggle(key: DictionnaryKey): void

    install(app: App): void
}

declare module '@vue/runtime-core' {
    export interface ComponentCustomProperties {
        /** Current data saved under the VUE_SESSION_KEY */
        localStorage: object
        /** Current data saved under VUE_SESSION_KEY */
        sessionStorage: object
        /** The VueLocalStorage instance */
        $localstorage: VueLocalStorage
        /** The VueSession instance */
        $session: VueSession
    }
}
