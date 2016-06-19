using UnityEngine;
using System.Collections;

public class Ninja_StarController : MonoBehaviour {

    public float star_speed;

    public NewBehaviourScript scorpion;

	// Use this for initialization
	void Start () {
        scorpion = FindObjectOfType<NewBehaviourScript>();

        if(scorpion.transform.localScale.x < 0)
        {
            star_speed = -star_speed;
        }
	
	}
	
	// Update is called once per frame
	void Update () {
        GetComponent<Rigidbody2D>().velocity = new Vector2(star_speed, GetComponent<Rigidbody2D>().velocity.y);
	
	}

    void OnTriggerEnter2D(Collider2D star_collide)
    {
        if(star_collide.tag == "Enemy")
        {
            Destroy(star_collide.gameObject);
        }

        Destroy(gameObject);
    }
}
