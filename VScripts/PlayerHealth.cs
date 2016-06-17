using UnityEngine;
using System.Collections;

public class PlayerHealth : MonoBehaviour
{
    public static int health = 100;

    // Use this for initialization
    void Start()
    {
		SpawnController.isPlayerDead = false;

    }

    // Update is called once per frame
    void Update()
    {
        if (health <= 0)
        {
			SpawnController.isPlayerDead = true;
            Destroy(this.gameObject);
        }
    }
}