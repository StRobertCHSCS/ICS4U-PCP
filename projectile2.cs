using UnityEngine;
using System.Collections;

public class projectile2 : MonoBehaviour
{

    public float speed;

    public MarioController player;


    public LevelManager levelManager;
    public LevelManager2 levelManager2;

    // Use this for initialization
    void Start()
    {
        player = FindObjectOfType<MarioController>();

        if (player.GetComponent<Rigidbody2D>().velocity.x < 0)
            speed = -speed;

        levelManager = FindObjectOfType<LevelManager>();
        levelManager2 = FindObjectOfType<LevelManager2>();

    }

    // Update is called once per frame
    void Update()
    {
        GetComponent<Rigidbody2D>().velocity = new Vector2(speed, GetComponent<Rigidbody2D>().velocity.y);

    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.name == "mario")
        {
            levelManager.RespawnPlayer();
        }
        if (other.name == "mario2")
        {
            levelManager2.RespawnPlayer();
        }
        Destroy(gameObject);
    }
}