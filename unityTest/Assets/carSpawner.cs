using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class carSpawner : MonoBehaviour
{
    [SerializeField] private float spawnDelay = 10f;
    private float spawnDelayTimer = 0f;

    [SerializeField] private GameObject spawnPoint;
    [SerializeField] private GameObject car;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (spawnDelayTimer <= 0)
        {
            GameObject Car = Instantiate(car, spawnPoint.transform.position, spawnPoint.transform.rotation);
            spawnDelayTimer = spawnDelay;
        }
        else
        {
            spawnDelayTimer -= Time.deltaTime;
        }
    }
}
